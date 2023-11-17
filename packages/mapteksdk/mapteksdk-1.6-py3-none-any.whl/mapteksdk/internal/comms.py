"""Types for communicating with Maptek Applications.

The types for working with the communication layer in Maptek applications that
use the Master Control Program (MCP).

The primary type provided is the Message class. It is designed to be the base
class for classes that define the contents of a message to be sent or
received. The types of the fields in the message can be:
- bool
- float
- str
- ctypes for integers (e.g ctypes.c_int16 and ctypes.c_uint32)
- other types provided by this module (e.g. Icon and JsonValue)
- A tuple of types (e.g (ctypes.c_int8, c_types.c_int8, c_types.c_int16))
- InlineMessage
- Homogenous list - any of the types above may be used as the element type.

Here is a fictional example:
  class CreateNewUser(Message):
  '''Define the message known as CreateNewUser.

  This message can be used to create a new user within the system.
  '''
    message_name = 'CreateNewUser'
    name: str
    age: ctypes.c_int16
    address: str

Now to create the message and send it we do the following:
  new_user = CreateNewUser()
  new_user.name = 'Muffin Man'
  new_user.age = 28
  new_user.address = 'Drury Lane'
  new_user.send(destination='personnelServer')

*Defining a list within a message*

For example:
  from typing import List

  class Example(Message):
    ages: List[c_types.c_uint16]

*Defining a Request/Response message pair*
  class QueryUserFirstMatch(Request):
  '''Define the message known as QueryUserFirstMatch.

  This message can be used to find information about a user.
  '''
    class Response(Message):
      name: str,
      age: ctypes.c_int16
      address: str

    message_name = 'QueryUser'
    response_type = Response

    name: str

  query = QueryUserFirstMatch()
  query.name = 'Muffin*'
  user = query.send(destination='personnelServer')
  print(f'{user.name} lives at {user.address}')

*Defining a SubMessage*

This is similar to a message however it supports having a repeating field.
The repeating field is unique to sub-messages and is optional. Not every
sub-message type requires a repeating field. It is like a list but the
difference is instead of storing how many elements there are up front it
keeps reading until the end of the sub-message.

  class Group(SubMessage):
    division: str
    participants: comms.RepeatingField[str]

  class Office(Message):
    message_name = 'CommsTests.Office'

    name: str
    admin: Group
    address: str

  group = Group()
  group.division = 'Admin'
  group.participants = ['Cortana Googleton', 'Alexa Fabrikam']

  office = Office()
  office.name = 'Fourthcoffee HQ'
  office.admin = group
  office.address = 'Ninth Avenue'

Warnings
--------
Vendors and clients should not develop scripts or applications against
this package. The contents may change at any time without warning.
"""

###############################################################################
#
# (C) Copyright 2020, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

import contextlib
import ctypes
import typing
import logging

from mapteksdk.capi.mcp import Mcpd
from mapteksdk.capi.translation import Translation

LOGGER = logging.getLogger('mapteksdk.internal.comms')

T = typing.TypeVar('T')


class ReceivedSerialisedText:
  """Represents text received through the communication system.

  It differs from SerialisedText as the text template and arguments for it is
  opaque. It is not possible to query them.
  """
  def __init__(self, serialised_string):
    self.serialised_string = serialised_string

  def __repr__(self):
    return f'ReceivedSerialisedText("{self.serialised_string}")'

  @contextlib.contextmanager
  def to_text_handle(self):
    """Converts the text to a text_handle."""
    text_handle = Translation().FromSerialisedString(
      self.serialised_string.encode('utf-8'))

    try:
      yield text_handle
    finally:
      Translation().FreeText(text_handle)

  @classmethod
  def from_handle(cls: typing.Type[T], handle) -> T:
    """Read the message from a handle.

    This is useful when receiving a message from a sender.

    Returns
    -------
    cls
      A ReceivedSerialisedText rather than SerialisedText as the text template
      and parameters can't be queried.
    """
    text_handle = Mcpd().ExtractText(handle)
    try:
      return cls(Translation().ToSerialisedString(text_handle))
    finally:
      Translation().FreeText(text_handle)


class SerialisedText:
  """Represents text sent through the communication system.

  The two parts of it are the text template and the arguments, where arguments
  can be strings and numbers. The text template specify where they appear in
  the text and how they are formatted.

  Parameters may be a string, float, SerialisedText or a sequence of strings.
  If you want integers at this time, use %.0f and convert the parameter to a
  float.
  Sequences of strings allow for use of the %v format specification.
  Only strings are supported at this time.
  """

  def __init__(self, text_template, *parameters):
    if isinstance(text_template, SerialisedText):
      self.text_template = text_template.text_template
      self.parameters = text_template.parameters
    else:
      self.text_template = text_template
      self.parameters = parameters

      # Check parameters are the basic supported types.
      supported_parameter_types = (
        str,
        float,
        SerialisedText,
        typing.Sequence,
        )

      for index, parameter in enumerate(self.parameters):
        if not isinstance(parameter, supported_parameter_types):
          raise TypeError(f'Parameter {index + 1} is an unsupported type: '
                          + type(parameter).__name__)

  def __repr__(self):
    parameter_string = ','.join(str(parameter) for parameter in self.parameters)
    return f'SerialisedText("{self.text_template}", {parameter_string})'

  @contextlib.contextmanager
  def to_text_handle(self):
    """Converts the text to a text_handle."""
    text_handle = Translation().NewText(self.text_template.encode('utf-8'))
    # Add each of the arguments
    for index, parameter in enumerate(self.parameters):
      if isinstance(parameter, str):
        Translation().AddArgumentString(text_handle, parameter.encode('utf-8'))
      elif isinstance(parameter, float):
        Translation().AddArgumentDouble(text_handle, parameter)
      elif isinstance(parameter, SerialisedText):
        with parameter.to_text_handle() as inner_handle:
          Translation().AddArgumentText(text_handle, inner_handle)
      elif isinstance(parameter, typing.Sequence):
        Translation().AddArgumentStringVector(text_handle, parameter)
      else:
        Translation().FreeText(text_handle)
        raise TypeError(f'Parameter {index+1} is an unsupported type: '
                        + type(parameter).__name__)
    try:
      yield text_handle
    finally:
      Translation().FreeText(text_handle)


class RepeatingField(typing.Generic[T], typing.Sized):
  """Define a type in a message that repeats until the end of message.

  This enables list-like behaviour. However unlike a list which records
  how many elements are in it first so the receiver knows how many to look
  for instead the receiver reads until the end of the message/sub-message.
  There is no indicator about the end of a inline message so it can't be
  used in an inline message in general (it could be used if that inline
  message was at the end).
  """


class Message:
  """A base class for MCP messages.

  Derived types should specify the fields that make up the message using
  instance variables annotations (PEP-526). The general form of which are:
     name: type
     name: type = default

  name should be a str and a valid Python identifier.
  type should be bool, str, a suitable type from ctypes for integers and
  floating-point numbers or a class which provides a convert() function for
  converting to one of the fundamental types, or another message type.

  If you wish to annotate the type of class variables, use ClassVar from
  typing module.

  Fields whose name starts with an underscore will not be sent when the
  message is sent (and thus, also won't be received).

  Attributes
  ----------
  message_name : str
    The name of the request. This name must not include two colons (::).
  """

  message_name: typing.ClassVar[str] = ''

  def send(self, destination):
    """Send the message to the destination.

    Parameters
    ----------
    destination : str
      The destination of where to send the message.
    """

    assert self.message_name.strip(), 'The name of the message is required.'
    assert '::' not in self.message_name, 'The name may not contain ::'

    if not destination:
      raise ValueError('No destination specified.')

    LOGGER.info('Sending %s to %s', self.message_name, destination)
    message = self._build_message(destination, is_request=False)
    Mcpd().dll.McpSend(message)

  @classmethod
  def from_handle(cls: typing.Type[T], handle) -> T:
    """Read the message from a handle.

    This is useful when receiving a message from a sender.

    Returns
    -------
    cls
      A message object populated with the values from the given handle.
    """
    return _extract_fields(handle, cls)

  def _build_message(self, destination, is_request):
    """Build the message to be sent to the given destination.

    This uses the definition of fields provided on the class to build the
    message with expected data.

    Parameters
    ----------
    destination : str
      The destination to send the message.
    is_request : bool
      Is the message a request/response style message or message with no
      immediate feedback?

    Returns
    -------
    T_MessageHandle
      The created message handle.
    """

    mcp = Mcpd().dll

    message = mcp.McpNewMessage(
      destination.encode('utf-8'),
      self.message_name.encode('utf-8'),
      is_request)

    assert message.value

    _add_content_to_message(message, self)

    return message


class InlineMessage:
  """A base class for types that are used within a Message.

  The inline nature is referring to the fact that the fields will be added
  to the message one another another without being contained within a group.

  For example consider the following types:
    class Person(InlineMessage):
      name: str
      email: str

    class Employee(Message):
      employee: Person
      manager: Person

    class EmployeeAlt(Message):
      employee_name: str
      employee_email: str
      manager_name: str
      manager_email: str

    Employee and EmployeeAlt are equivalent, they both send and receive the
    same messages so you could send a message with one type and receive it
    with the other.

  Derived types should specify the fields that make up the message using
  instance variable annotations (PEP-526), as seen in the examples above.
  The general form of of which are:
     name: type
     name: type = default

  name should be a str and a valid Python identifier.
  type should be bool, str, a suitable type from ctypes for integers and
  floating-point numbers or a class which provides a convert() function for
  converting to one of the fundamental types, or another message type.

  If you wish to annotate the type of class variables, use ClassVar from
  typing module.
  """

  # Derived classes should have a fields attribute described like so:
  #   name: type
  #   name: type = default

  @classmethod
  def from_handle(cls: typing.Type[T], handle) -> T:
    """Read the message from a handle.

    Returns
    -------
    cls
      A message object populated with the values from the given handle.
    """
    return _extract_fields(handle, cls)


class SubMessage:
  """Provides a logical grouping of data which gets preserved across
  the communication system.

  In comparison to an inline message think of a sub-message as having a
  marker at the start to flag the start of a sub-message, where as inline
  message is the same as if the children were part of the outer message.

  A unique feature of a sub-message is support for having a repeating_field
  which enables list-like behaviour. However unlike a list which records
  how many elements are in it first so the receiver knows how many to look
  for instead the receiver reads until the end of the sub-message.

  Like Message and Inline message it requires annotating instance variables
  to specify their type and thus describe what fields there are. See Message
  for more information.

  See Also
  --------
  Message : Very similar. They are sendable as well.
  InlineMessage : Provides a logical group which isn't preserved across
                  communication.
  """

  @classmethod
  def from_handle(cls: typing.Type[T], handle) -> T:
    """Read the message from a handle.

    This is useful when receiving a message from a sender.

    Returns
    -------
    cls
      A message object populated with the values from the given handle.

    Raises
    ------
    TypeError
      If handle does not start at a sub-message.
    """

    mcp = Mcpd().dll

    if mcp.McpIsSubMessage(handle):
      handle = mcp.McpExtractSubMessage(handle)
      did_extract_sub_message = True
    else:
      # Assume handle is the sub-message itself. There is no way to check this
      # through the C API.
      handle = handle
      did_extract_sub_message = False

    try:
      message = _extract_fields(handle, cls)

      repeating_field = cls.find_repeating_field()
      if repeating_field:
        field_type = repeating_field[1]
        message_types = (Message, SubMessage, InlineMessage)
        values = []
        if field_type is typing.Any:
          # Reading repeating fields of the Any type is not yet implemented.
          # Setting this to NotImplemented makes it very obvious in the debugger
          # why the expected values are not present.
          values = NotImplemented
        elif issubclass(field_type, message_types):
          while not mcp.McpIsEom(handle):
            values.append(_extract_fields(handle, field_type))
        else:
          while not mcp.McpIsEom(handle):
            values.append(_extract_value_from_message(handle, field_type))
        setattr(message, repeating_field[0], values)

      return message
    finally:
      if did_extract_sub_message:
        mcp.McpFreeMessage(handle)

  @classmethod
  def find_repeating_field(cls):
    """Return the name and type of the repeating field if present.

    Returns
    -------
    None
      if there is no repeating field present.
    tuple (str, type)
      The name and type of the repeating field that was present.

    Raises
    ------
    ValueError
      If more than one repeating field is present.
    ValueError
      If there is not exactly one type specified for the RepeatingField.
    """

    annotations = getattr(cls, '__annotations__', {})

    def is_repeating_field(field_type):
      origin = getattr(field_type, '__origin__', type(None))
      if origin is typing.ClassVar:
        return False
      return issubclass(origin, RepeatingField)

    if sum(1 for sub_field_type in annotations.values()
           if is_repeating_field(sub_field_type)) > 1:
      raise ValueError("A message type must only have a single repeating "
                       "field.")

    try:
      name, generic_type = next(
        (field_name, sub_field_type)
        for field_name, sub_field_type in annotations.items()
        if is_repeating_field(sub_field_type))
    except StopIteration:
      # There is no repeating field.
      return None

    if len(generic_type.__args__) != 1:
      raise ValueError("A repeating field must have a single type specified.")

    return (name, generic_type.__args__[0])

  @contextlib.contextmanager
  def to_message_handle(self):
    """Converts the message into a handle to the sub-message in C++.

    See Also
    --------
    SerialisedText.to_text_handle :  Similar function but for text.
    """
    mcp = Mcpd().dll
    sub_message = mcp.McpNewSubMessage()

    _add_content_to_sub_message(sub_message, type(self), self)

    try:
      yield sub_message
    finally:
      Mcpd().dll.McpFreeMessage(sub_message)


class Request(Message):
  """A MCP message which forms a request that expects a response back.

  This provides special case handling for this scenario. It is often
  possible to mimic this behaviour by listening for a message that forms
  the reply and then sending an message which will elicit the message
  being sent back.
  """

  message_name: typing.ClassVar[str] = ''
  """The name of the message.

  Derived classes should override this field.
  """

  response_type: typing.ClassVar[typing.Union[type, None]] = None
  """The type of the response.

  Derived classes should override this field
  """

  def send(self, destination):
    """Sends the request to the destination and waits for the response back."""

    assert self.message_name.strip(), 'The name of the message is required.'
    assert '::' not in self.message_name, 'The name may not contain ::'

    if not destination:
      raise ValueError('No destination specified.')

    LOGGER.info('Requesting %s of %s', self.message_name, destination)
    message = self._build_message(destination, is_request=True)
    response = Mcpd().dll.McpSendAndGetResponseBlocking(message)
    LOGGER.info('Received response back for %s from %s',
                self.message_name, destination)
    decoded_response = self.response_type.from_handle(response)
    Mcpd().dll.McpFreeMessage(response)
    return decoded_response


def request_no_body(message_name: str, response_type: type) -> Request:
  """Creates a request with no body.

  This is useful for requests which have no body (i.e no parameters) as
  the destination and message name provides everything it needs.

  Parameters
  ----------
  message_name
    A non-empty string representing the name of the message to send.
  response_type
    The response type which is typically a class that inherits from Message.

  Returns
  -------
  Request
      A request instance with no parameters but a message name.
  """
  assert message_name
  request = Request()

  # While the message name and response type are typically class variables
  # it was intended to allow them to be overridden on a per-instance basis.
  request.message_name = message_name
  request.response_type = response_type
  return request


def _add_content_to_message(message, content):
  """Adds the content of a message type (Message, InlineMessage) to the MCP
  message specified by message.

  The message type is expected to have a fields member which lists the fields
  that make up the message. For each field, this looks-up the value of the
  field from content and appends it to the message.

  Parameters
  ----------
  message : T_MessageHandle
    The handle to an MCP message from the C API.
  content : Message or InlineMessage
    The content to add to the message.
  """

  def append_single_value(message, field_type, raw_value):
    # Convert the raw value to the expected type. For example, this converts
    # a value of type int to one of type ctypes.c_int16.
    convert_to_storage_type = getattr(field_type, 'convert_to', None)
    if convert_to_storage_type:
      field_value = convert_to_storage_type(raw_value)
    else:
      if not isinstance(raw_value, field_type):
        field_value = field_type(raw_value)
      else:
        field_value = raw_value

    _append_value_to_message(message, field_value)

  # Determine the list of fields of the message from the annotations.
  annotations = getattr(content, '__annotations__', {})

  # Ignore repeating fields and class variables.
  def ignore_annotation(field_type):
    origin = getattr(field_type, '__origin__', type(None))
    return origin is typing.ClassVar or issubclass(origin, RepeatingField)

  fields = list(
    (field_name, field_type)
    for field_name, field_type in annotations.items()
    if not ignore_annotation(field_type))

  for field in fields:
    field_name, field_type = field

    # Fields which start with an underscore should not be sent over the MCP.
    if field_name.startswith("_"):
      continue

    # Default values are naturally handled by the Python language as new
    # instances of the message class will have a field with the default value.
    raw_value = getattr(content, field_name)

    # If the field type is specified via a type-alias, use the type from
    # it.
    origin = getattr(field_type, '__origin__', None)
    if origin is not None:
      # This accounts for if field_type is typing.List[bool] such that
      # storage_type will be list and field_type remains as the full-type.
      storage_type = origin
    else:
      storage_type = getattr(field_type, 'storage_type', field_type)

    if field_type is typing.Any:
      # In this case it is assumed the value tells us what it is.
      if isinstance(raw_value, (Message, SubMessage, InlineMessage)):
        _add_content_to_message(message, raw_value)
      else:
        # We could possibly open this up to ctypes and anything
        # _append_value_to_message supports.
        raise TypeError('The value of an Any must be a message type.')
    elif storage_type and issubclass(storage_type, (list, set)):
      # The type of the elements comes from the arguments of the type.
      if len(field_type.__args__) != 1:
        raise ValueError(
          f'The type {field_type.__name__} should only specify one type '
          f'for the {storage_type.__name__}.')

      element_type = field_type.__args__[0]

      # Send the size
      append_single_value(message, ctypes.c_uint64, len(raw_value))

      # Then send each of the values.
      for sub_value in raw_value:
        if isinstance(sub_value, InlineMessage):
          _add_content_to_message(message, sub_value)
        else:
          append_single_value(message, element_type, sub_value)
    elif storage_type and issubclass(storage_type, tuple):
      for sub_value, sub_type, in zip(raw_value, field_type.__args__):
        append_single_value(message, sub_type, sub_value)
    elif issubclass(storage_type, InlineMessage):
      _add_content_to_message(message, raw_value)
    elif issubclass(storage_type, SubMessage):
      with raw_value.to_message_handle() as sub_message:
        mcp = Mcpd().dll
        mcp.McpAppendSubMessage(message, sub_message)
    elif issubclass(storage_type, Message):
      # This case could be treated as either an inline message or a
      # sub-message.
      raise NotImplementedError('Nesting a Message in another message')
    else:
      append_single_value(message, field_type, raw_value)

  return message


def _add_content_to_sub_message(sub_message, field_type, value):
  """Add a sub-message from the given value and appends it to the message.

  Parameters
  ----------
  sub_message : T_MessageHandle
    The sub message to append to.
  field_type : type
    The type that derives from SubMessage
  value : SubMessage
    The value to append to the message.

  Raises
  ------
  TypeError
    If value contains a type that isn't supported.
  """
  # Sink in the known fields first.
  _add_content_to_message(sub_message, value)

  message_types = (Message, SubMessage, InlineMessage)

  # Sink in the repeating field (essentially a list) after. This must come
  # last as the only way to know when there are no more fields is to detect
  # the end of the sub-message on the receiving end.
  repeating_field = getattr(field_type, 'find_repeating_field',
                            lambda: None)()

  if repeating_field and repeating_field[1] is typing.Any:
    repeat_values = getattr(value, repeating_field[0])
    for sub_value in repeat_values:
      if isinstance(sub_value, message_types):
        _add_content_to_message(sub_message, sub_value)
      else:
        # This will raise a TypeError if the value type is not supported.
        _append_value_to_message(sub_message, sub_value)
  elif repeating_field and issubclass(repeating_field[1], message_types):
    repeating_values = getattr(value, repeating_field[0])
    for sub_value in repeating_values:
      _add_content_to_message(sub_message, sub_value)
  elif repeating_field:
    repeating_field_type = repeating_field[1]
    repeating_values = getattr(value, repeating_field[0])
    convert_to_storage_type = getattr(repeating_field_type, 'convert_to',
                                      None)
    for sub_value in repeating_values:
      # Convert the raw value to the expected type. For example, this converts
      # a value of type int to one of type ctypes.c_int16.
      if convert_to_storage_type:
        field_sub_value = convert_to_storage_type(sub_value)
      elif isinstance(sub_value, repeating_field_type):
        field_sub_value = sub_value
      else:
        field_sub_value = repeating_field_type(sub_value)
      _append_value_to_message(sub_message, field_sub_value)


def _append_value_to_message(message, value):
  """Append message with the given value.

  Parameters
  ----------
  message : T_MessageHandle
    The message to append to.
  value
    The value to append to the message.

  Raises
  ------
  TypeError
    If value is a type that isn't supported.
  """
  mcp = Mcpd().dll

  if isinstance(value, float):
    raise TypeError('float is ambiguous, use ctypes.c_float or '
                    'ctypes.c_double')

  signed_integer_types = (ctypes.c_int8, ctypes.c_int16, ctypes.c_int32,
                          ctypes.c_int64)
  unsigned_integer_types = (ctypes.c_uint8, ctypes.c_uint16,
                            ctypes.c_uint32, ctypes.c_uint64)

  if isinstance(value, bool):
    mcp.McpAppendBool(message.value, value)
  elif isinstance(value, ctypes.c_float):
    mcp.McpAppendFloat(message, value)
  elif isinstance(value, ctypes.c_double):
    mcp.McpAppendDouble(message, value)
  elif isinstance(value, str):
    mcp.McpAppendString(message, value.encode('utf-8'))
  elif isinstance(value, signed_integer_types):
    mcp.McpAppendSInt(message, value.value, ctypes.sizeof(value))
  elif isinstance(value, unsigned_integer_types):
    mcp.McpAppendUInt(message, value.value, ctypes.sizeof(value))
  elif isinstance(value, SerialisedText):
    with value.to_text_handle() as text_handle:
      mcp.McpAppendText(message, text_handle)
  else:
    raise TypeError(f'Unsupported type {type(value)}')


def _extract_fields(handle, message_type: typing.Type[T]) -> T:
  """Extract fields from a message handle and stores the result on message.

  Parameters
  ----------
  handle : T_MessageHandle
    The handle for the message to extract from.
  message_type : type
    The type that represents a message.

  Returns
  -------
  cls
    A message object populated with the values from the given handle.

  Raises
  ------
  TypeError
    If value is a type that isn't supported.
  """
  message = message_type()

  # Determine the list of fields of the message from the annotations.
  annotations = getattr(message_type, '__annotations__', {})

  # Ignore repeating fields and class variables.
  def ignore_annotation(field_type):
    origin = getattr(field_type, '__origin__', type(None))
    return origin is typing.ClassVar or issubclass(origin, RepeatingField)

  fields = list(
    (field_name, field_type)
    for field_name, field_type in annotations.items()
    if not ignore_annotation(field_type))

  for field_name, field_type in fields:
    # Fields starting with an underscore are not sent, so should not
    # be read.
    if field_name.startswith("_"):
      continue

    field_value = _extract_value_from_message(handle, field_type)
    LOGGER.debug('Extracted field %s from message with value %s',
                 field_name, field_value)
    setattr(message, field_name, field_value)

  return message


def _extract_value_from_message(message, value_type):
  """Extract a value from the message given its type.

  The resulting value won't necessarily be of the given type but will be
  convertible to it.

  Parameters
  ----------
  message : T_MessageHandle
    The message to extract from.
  value_type : type
    The expected type of the next value in the message.

  Raises
  ------
  TypeError
    If value is a type that isn't supported.
  """
  mcp = Mcpd().dll

  def _extract_string(message):
    string_length = mcp.McpGetNextStringLength(message)
    if string_length == 0:
      mcp.McpExtractString(message, ctypes.c_char_p(), string_length)
      return ''

    string_buffer = ctypes.create_string_buffer(string_length)
    mcp.McpExtractString(message, string_buffer, string_length)
    return string_buffer.value.decode('utf-8')

  # If the field type is specified via a type-alias, use the type from
  # it.
  origin = getattr(value_type, '__origin__', None)
  if origin is not None:
    storage_type = getattr(origin, 'storage_type', None) or origin
    assert storage_type
  else:
    storage_type = getattr(value_type, 'storage_type', None)

  if storage_type:
    if issubclass(storage_type, (list, set)):
      size = _extract_value_from_message(message, ctypes.c_uint64)

      # The type of the elements comes from the arguments of the type.
      if len(value_type.__args__) != 1:
        raise ValueError(
          f'The type {value_type.__name__} should specify one type for '
          f'the {storage_type.__name__}.')

      element_type = value_type.__args__[0]

      return storage_type(
        _extract_value_from_message(message, element_type)
        for _ in range(size)
      )
    if issubclass(storage_type, tuple):
      return tuple(
        _extract_value_from_message(message, element_type)
        for element_type in value_type.__args__
      )

    native_value = _extract_value_from_message(message, storage_type)
    return value_type.convert_from(native_value)

  if issubclass(value_type, (SerialisedText, ReceivedSerialisedText)):
    # This must be a ReceivedSerialisedText as its not possible to
    # represent it as SerialisedText because the text template and
    # parameters can't be extracted.
    return ReceivedSerialisedText.from_handle(message)

  message_types = (InlineMessage, Message, SubMessage)
  if issubclass(value_type, message_types):
    return value_type.from_handle(message)

  if issubclass(value_type, bool):
    return mcp.McpExtractBool(message)

  if issubclass(value_type, str):
    return _extract_string(message)

  float_types = (float, ctypes.c_float, ctypes.c_double)
  if issubclass(value_type, float_types):
    return mcp.McpExtractFloat(message)

  signed_integer_types = (ctypes.c_int8, ctypes.c_int16, ctypes.c_int32,
                          ctypes.c_int64)
  if issubclass(value_type, signed_integer_types):
    return mcp.McpExtractSInt(message)

  unsigned_integer_types = (ctypes.c_uint8, ctypes.c_uint16,
                            ctypes.c_uint32, ctypes.c_uint64)
  if issubclass(value_type, unsigned_integer_types):
    return mcp.McpExtractUInt(message)

  raise TypeError(f'Unsupported type {value_type}')

"""Exceptions intended to be thrown in tests."""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

class ArtificialError(Exception):
  """Raised by tests to test handling of errors.

  The problem:
  Consider the following test case:

  >>> with self.assertRaises(RuntimeError):
  >>>     do_something()
  >>>     raise RuntimeError("Make sure an error occurs")
  >>> check_do_something_was_cancelled_due_to_error()

  If the do_something() function raises a RuntimeError, the above test
  may pass when it should fail.

  The solution:
  This error is only raised in tests, so it can be used to make sure
  the above problem does not occur:

  >>> with self.assertRaises(ArtificialError):
  >>>     do_something()
  >>>     raise ArtificialError("Make sure an error occurs")
  >>> check_do_something_was_cancelled_due_to_error()
  """

class TestTimeoutError(Exception):
  """Error raised when a test times out."""

class MessageSequenceError(Exception):
  """Error raised when a message arrives out of sequence."""

class MessageValueError(Exception):
  """Error raised for right type of message, but wrong contents."""

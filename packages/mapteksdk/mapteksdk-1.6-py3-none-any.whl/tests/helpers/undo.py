"""Trigger undo from Python.

This is part of the tests because it is not expected to be something
users should be doing, but it is useful for testing undo against a
running application.
"""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

import ctypes
import itertools

from mapteksdk.internal.comms import InlineMessage, SubMessage
from mapteksdk.internal.transaction_manager import (
  TransactionCreate, TransactionRequestData)
from mapteksdk.internal.qualifiers import (
  Qualifiers, QualifierSet, InstanceTypes)

TOKEN = itertools.count(start=1)
"""Used to give each request a unique transaction token."""

class DummySubMessage(SubMessage):
  """A dummy sub message.

  This adds an extra empty serC_DataGroup at the end of the message.
  The message doesn't trigger an undo without the extra empty group.
  """

class DummyData(InlineMessage):
  """Dummy data for the undo message."""
  message: DummySubMessage

def undo():
  """Tell the application to press undo."""
  qualifiers = QualifierSet()
  qualifiers.values = [
    Qualifiers.instance_type(InstanceTypes.UNDO)
  ]

  dummy_sub_message = DummySubMessage()
  initial_data = DummyData()
  initial_data.message = dummy_sub_message

  request_data = TransactionRequestData()
  request_data.class_name = "mdf::uiC_UndoTransaction"
  request_data.data_type_name = "mdf::serC_DataGroup"
  request_data.transaction_address = ctypes.c_uint64(24)
  request_data.transaction_token = ctypes.c_uint64(next(TOKEN))
  request_data.qualifiers = qualifiers

  message = TransactionCreate()
  message.transaction_manager_address = ctypes.c_uint64(42)
  message.request_data = request_data
  message.initial_value = initial_data
  response = message.send("uiServer")

  if not response.success:
    raise RuntimeError("Failed to trigger undo.")

def redo():
  """Tell the application to press redo."""
  qualifiers = QualifierSet()
  qualifiers.values = [
    Qualifiers.instance_type(InstanceTypes.REDO)
  ]

  dummy_sub_message = DummySubMessage()
  initial_data = DummyData()
  initial_data.message = dummy_sub_message

  request_data = TransactionRequestData()
  request_data.class_name = "mdf::uiC_RedoTransaction"
  request_data.data_type_name = "mdf::serC_DataGroup"
  request_data.transaction_address = ctypes.c_uint64(24)
  request_data.transaction_token = ctypes.c_uint64(next(TOKEN))
  request_data.qualifiers = qualifiers

  message = TransactionCreate()
  message.transaction_manager_address = ctypes.c_uint64(42)
  message.request_data = request_data
  message.initial_value = initial_data
  response = message.send("uiServer")

  if not response.success:
    raise RuntimeError("Failed to trigger redo.")

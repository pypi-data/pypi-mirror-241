"""Workflow specific helper functions and classes."""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
from __future__ import annotations

import os
import json
import tempfile
import typing

from mapteksdk.workflows import WorkflowArgumentParser, ConnectorType

class OutputConnector(typing.NamedTuple):
  """Class used in tests to declare output connectors.

  The output_connector_test_helper_shared() function below uses
  this to declare output connectors with the specified name and type,
  and then sets the specified value to the connector.
  """
  name: str
  """The name of the connector to declare."""
  value: typing.Any
  """The value to assign to the output connector."""
  connector_type: type[ConnectorType]
  """The type to assign to the output connector."""


def output_connector_test_helper_shared(
    output_connectors: list[OutputConnector]):
  """Does the heavy lifting for testing output connectors.

  Parameters
  ----------
  output_connectors
    A list of output connector named tuples representing the output connectors
    to create and the values to assign to each.

  Returns
  -------
  dict
    JSON dictionary written out by the output connectors.

  """
  with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as json_file:
    args = [f"--workflow-output-path={json_file.name}"]
    parser = WorkflowArgumentParser()
    for connector in output_connectors:
      parser.declare_output_connector(connector.name, connector.connector_type)
    parser.parse_arguments(args)
    for connector in output_connectors:
      parser.set_output(connector.name, connector.value)

    parser.flush_output()
    result = json.load(json_file)

  try:
    os.remove(json_file.name)
  except OSError:
    pass

  return result

"""Access and resolve the test data."""
###############################################################################
#
# (C) Copyright 2022, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
from __future__ import annotations

import importlib.util
import os
import pathlib

MODULE_PATH = pathlib.Path(__file__)

def get_test_data_path() -> pathlib.Path:
  """Get the path the temporary maptekdb is stored in during testing."""
  test_data_path = MODULE_PATH.parent.parent / "test_data"
  # Ensure the directory exists.
  os.makedirs(test_data_path, exist_ok=True)
  return test_data_path

def resolve_test_data(filename: str | pathlib.Path, extract: bool=False):
  """Resolves the given reference file to the actual file.

  This uses the testdata module for Git-Kit to fetch a file from the binary
  resource system, as we do not keep test data in Git.

  If your test is going to be modifying the file, it should first copy it to a
  temporary file/directory first.

  Parameters
  ----------
  filename
    If this is a string, this is the name of a .ref file in the data
    sub-directory to resolve.
    If this is a Path, this is the full path to a .ref file to resolve.

  extract
    Attempt to extract the given file, provided it is a supported archive
    format. The path returned will be to the extracted folder.

  Returns
  -------
  str
    The resolved (dereferneced) path to the test data. This most likely refers
    to a file in the Git-Kit binary cache.
  """

  def _load_testdata_module():
    workspace_root = MODULE_PATH.parent.parent.parent.parent
    module_path = workspace_root / "tools" / "python" / "testdata.py"

    spec = importlib.util.spec_from_file_location('testdata', module_path)
    testdata = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(testdata)
    return testdata

  testdata = _load_testdata_module()

  if isinstance(filename, str):
    reference = MODULE_PATH.parent.parent / "data" / filename
  elif isinstance(filename, pathlib.Path):
    reference = filename
  else:
    raise TypeError(f"Unsupported value for filename: {filename}")

  # Check if the file is already cached first.
  path = testdata.cachedFileLookup(reference, os.getenv('GITKIT_BINARY_CACHE'),
    extract)
  if path:
    return path

  # Fetch the download service information and cache it for subsequent calls.
  download_service = getattr(resolve_test_data, 'download_service', None)
  if not download_service:
    service_uri = os.getenv('GITKIT_SERVICE_URI')
    if not service_uri:
      raise ValueError('No environment variable "GITKIT_SERVICE_URI"' +
                       ' defined ')

    # pylint: disable=protected-access
    entry_point = testdata._getServices(service_uri)
    download_service = entry_point['getResource']
    resolve_test_data.download_service = download_service

  return testdata.cacheFile(
    reference, os.getenv('GITKIT_BINARY_CACHE'), download_service,
    extract=extract)

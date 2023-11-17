"""Module for working with a pre-built application for testing.

This module can be run as a script which will allow it to fetch and extract
the application from a MSI (that has been referenced via testdata).
"""

import argparse
import os
import pathlib
import shutil
import stat
import subprocess
import sys

from tests.helpers.testdata import resolve_test_data


def fetch_installer(reference) -> pathlib.Path:
  """Fetch the installer from the given reference file.

  Parameters
  ----------
  reference
    The name of the reference containing the installer.
    This is expected to be in the data sub-directory.

  Returns
  -------
  pathlib.Path
      The path to the installer in the binary cache.
  """
  # The testdata module is not able to extract MSI (it is outside the
  # scope of that module).
  installer = resolve_test_data(reference, extract=False)
  return pathlib.Path(installer)


def extract_application(installer, destination: pathlib.Path) -> pathlib.Path:
  """Extract the application from its installer.

  This uses lessmsi from: https://github.com/activescott/lessmsi/releases/

  Parameters
  ----------
  installer
    The path to the installer of the application to extract.
  destination
    The path to extract the installer into.

  Returns
  -------
  pathlib.Path
    The path that the installer was extracted into.
  """
  script_directory = pathlib.Path(__file__).absolute().parent
  lessmsi_directory = resolve_test_data(
      script_directory / '..' / 'data' / 'lessmsi-v1.10.0.zip.ref',
      extract=True)
  lessmsi = pathlib.Path(lessmsi_directory) / 'lessmsi.exe'

  if not lessmsi.is_file():
    raise ValueError(f'Could not find "{lessmsi}"')

  if not destination.exists():
    destination.mkdir()

  # x means Extract all the files in the specified msi.
  # lessmsi requires the destination path end in a \ so it knows it is a
  # directory.
  subprocess.check_call(
    [str(lessmsi), 'x', str(installer), str(destination) + '\\']
  )

  return destination


def delete_extracted_application(path: pathlib.Path):
  """Delete the extracted application.

  This accounts for files being set to read-only. For example the help file
  found in PointStudio.
  """
  def on_error(function, path, exception_information):
    """When rmtree encounters an error attempt to fix it."""
    if sys.version_info < (3, 12):
      # Prior to 3.12, the third argument was a tuple from sys.exc_info().
      exception_information = exception_information[1]

    if isinstance(exception_information, PermissionError):
      # The file may be set to read-only. The icon file in a Maptek
      # Database is one such file.
      os.chmod(path, stat.S_IWRITE)
      function(path)
      return

    # pylint: disable=misplaced-bare-raise;reason=Function is called within
    # an except block inside of shutil.rmtree.
    raise

  if sys.version_info >= (3, 12):
    shutil.rmtree(str(path), onexc=on_error)
  else:
    shutil.rmtree(str(path), onerror=on_error)


def main():
  """Provides a command line interface for fetch and extract the application.
  """
  parser = argparse.ArgumentParser(
    description="Fetch and extract the given application from the "
                "reference file.",
  )
  parser.add_argument(
    'installer_reference',
    help='The name of reference file containing an application. '
         'The reference file is expected to be in the data/ '
         'sub-directory.',
    )
  parser.add_argument(
    'destination',
    help='The path to extract the application to.',
    )

  arguments = parser.parse_args()
  destination = pathlib.Path(arguments.destination)

  installer = fetch_installer(arguments.installer_reference)

  if destination.is_dir() and destination.glob('**'):
    delete_extracted_application(destination)

  extract_application(installer, destination)

  # The result is provided as-is, no tidying up of the directory
  # structure is done.


if __name__ == '__main__':
  main()

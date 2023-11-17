"""Unit test helpers to build a test project and start a new mcpd instance
for running all tests against.

"""
###############################################################################
#
# (C) Copyright 2020, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

from __future__ import annotations

import datetime
import logging
import os
import pathlib

from mapteksdk.capi.license import License
from mapteksdk.internal.mcp import (Mcpd, McpdConnection, connect_to_mcpd,
                                    ConnectionFailedError)
from mapteksdk.project import Project
from mapteksdk.internal.options import (ProjectOptions, ProjectOpenMode)
from mapteksdk.internal import account

from .testdata import get_test_data_path, resolve_test_data

TEST_PROJECT = "test.maptekdb"
MDF_BUILD_PATH = "build\\windows_x64_msvc14_debug\\mdf\\"
MODULE_PATH = pathlib.Path(__file__)


class McpdFailedToStartError(Exception):
  """Error raised when the mcpd fails to start."""
  def __init__(self, exit_code):
    super().__init__('Failed to start mcpd.exe, it exited with code: '
                     f'{exit_code}')


def clean_up(test_project, allow_standard_containers=False):
  """Clean up the project to make it suitable for running another test.

  Remove any non-hidden and non-orphans from the project. This makes
  the tests less likely to interact with one another. For example, test B
  won't expect test A has created an object that it uses.

  The selection is also cleared.

  If allow_standard_containers is true, this will also remove standard
  containers. Otherwise the standard containers will remain.

  """
  for name, object_id in test_project.get_children():
    if not name.startswith('.'):
      test_project.delete(object_id, allow_standard_containers)

  # Empty the recycle bin between tests.
  test_project.delete(test_project.recycle_bin_id)

  # Make sure selections don't persist between requests.
  test_project.set_selected(None)

def create_test_project(options=None):
  """Create in-memory project ready for unit tests.

  Parameters
  ----------
  options : ProjectOptions
    (optional) set of options to specify the
    settings used to connect to a data backend
    and/or host application.

  Returns
  -------
  Project
    Project ready for unit tests.

  """
  if options is None:
    options = get_test_project_options()
  test_proj = Project(options)
  # Note: to run against a host like Eureka, just call test_proj = Project()
  return test_proj

def get_test_base_path():
  """Get relative path to the running .py for ../test_data/."""
  root_path = MODULE_PATH.parent.parent.parent.parent
  return root_path / MDF_BUILD_PATH

def get_test_project_options():
  """Creates instance of ProjectOptions for test project purposes."""

  application_bin = os.environ.get('APPLICATION_BIN', default=None)
  if application_bin:
    options = ProjectOptions(
      str(get_test_data_path() / TEST_PROJECT),
      open_mode=ProjectOpenMode.MEMORY_ONLY,
      dll_path=application_bin,
    )
  else:
    options = ProjectOptions(
      str(get_test_data_path() / TEST_PROJECT),
      open_mode=ProjectOpenMode.MEMORY_ONLY,
      dll_path=str(get_test_base_path() / 'shlib'),
    )

  # The following credentials are only valid for the test instance.
  #
  # They expect the AccountBrokerPreferences.xml to be changed to point at
  # a different Maptek Account end-point.
  #
  # To avoid confusion for a developer that isn't signed in, we only do the
  # following on a test machine.
  if os.environ.get('MTK_TESTER'):
    options.account_broker_session_parameters = {
      'MaptekAccountUserName': 'sean.donnellan+testing@maptek.com.au',
      'MaptekAccountAuthKey': 'posX8q6vLC2qvXixjawO',

      # If the credentials provided above fail, we don't want the broker to
      # try to show a login window.
      'AllowInteractiveLogin': False,
    }

  # The tests aren't run against the package built from setuptools but are run
  # in-place as such the account broker DLLs aren't where they would normally
  # be.
  broker_interface_path = (
    MODULE_PATH.parent.parent.parent / "MaptekAccountBrokerInterfaces.zip.ref")

  broker_interface_path = resolve_test_data(
    broker_interface_path,
    extract=True,
    )
  options.account_broker_connector_path = broker_interface_path

  return options

def get_test_viewer_only_project_options():
  """Creates instance of ProjectOptions for testing mcpd spawning."""
  return ProjectOptions(
    str(get_test_data_path() / TEST_PROJECT),
    open_mode=ProjectOpenMode.CREATE_NEW,
    dll_path=str(get_test_base_path() / "shlib"),
  )

def spawn_mcpd(options: ProjectOptions) -> tuple[Mcpd, McpdConnection]:
  """Spawn the master control program daemon (mcpd) for testing.

  The caller is responsible for calling register_dll_directory().

  This connects to the Maptek Account broker to acquire a licence.

  These tests don't support being run offline (i.e to use borrowed
  licences).

  Parameters
  ----------
  options
    The options for using the broker.

  Returns
  -------
  Mcpd
    The handle over the newly spawned mcpd.
  McpdConnection
    A connection on the current thread to the newly spawned mcpd.

  Raises
  ------
  McpdFailedToStartError
    If a problem is detected with starting the mcpd and it can't be connected
    to.
  ValueError
    If options.dll_path is not set.
  """
  broker = account.connect_to_maptek_account_broker(
    options.account_broker_connector_path,
    options.account_broker_session_parameters)

  # A licence with the MDF140 feature code is required to start and use the
  # mcpd rather than the typical Extend licence.
  product = broker.product_information(
    name='SDKComms',
    display_name='SDK Communication Tests',
    version_label='1.0',
    license_format=License().supported_licence_format(),
    release_date=datetime.datetime.now(),
    )

  # The PointStudio feature code is also required as otherwise Maptek Account
  # can't find a suitable entitlement. We don't have a special entitlement
  # for just doing this. We could potentially create a licence that had both
  # SDK (Extend) and MDF140 for testing purposes.
  try:
    with broker.acquire_licence(product, ['MDF140', 'PointStudio']) as licence:
      mcpd_licence_string = str(licence.license_string)

    with broker.acquire_extend_licence(
        License().supported_licence_format()) as licence:
      extend_licence_string = str(licence.license_string)
  finally:
    broker.disconnect()

  application_bin = os.environ.get('APPLICATION_BIN', default=None)
  if not application_bin:
    application_bin = str(get_test_base_path() / 'bin')

  if not options.dll_path:
    raise ValueError('options.dll_path must be set')

  # Spawn the master control program daemon (mcpd).
  mcpd = Mcpd(
    mcpd_path=application_bin,
    mcpd_licence=mcpd_licence_string,
    dll_path=options.dll_path,
  )

  # Rethink the following, as the idea was to have mcpd.instance provide an
  # ExistingMcpdInstance which allows the Project() class to connect to the
  # constructor.
  #
  # An advantage of the current approach used here is it can handle all the
  # licencing and we know right now if we are able to connect to the mcpd.
  log = logging.getLogger("mapteksdk.tests.project_helpers")
  log.info("Connect to spawned mcpd (%d)...", mcpd.instance.mcpd_process_id)

  try:
    connection = connect_to_mcpd(
      specific_mcpd=mcpd.instance,
      sdk_licence=extend_licence_string)
  except ConnectionFailedError as error:
    # Failing to connect to mcpd.exe typically means it failed to start in
    # this case rather than the connection part failed.
    #
    # Poll the exit code to make sure.
    exit_code = mcpd.mcpd_process.poll()
    if exit_code is not None:
      log.critical(
        "Failed to connect because mcpd.exe exited with code: %i (%#x)",
        exit_code, exit_code)
    else:
      # An exit code of None indicates mcpd.exe is still running.
      log.critical(
        "Failed to connect to mcpd.exe, but it seems to be running.")

    raise McpdFailedToStartError(exit_code) from error

  return mcpd, connection
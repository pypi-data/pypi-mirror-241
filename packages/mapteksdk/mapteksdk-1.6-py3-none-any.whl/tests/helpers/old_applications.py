"""Helpers functions for testing functionality against old applications."""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
from __future__ import annotations

import contextlib
import os
import typing

from mapteksdk.capi import Modelling
from mapteksdk.capi.util import CApiFunctionNotSupportedError

if typing.TYPE_CHECKING:
  from mapteksdk.capi.wrapper_base import WrapperBase

def requires_min_api_version(version: tuple[int, int]):
  """Decorate a test to indicate it requires at least the API version given.

  The decorator should only be applied to a bound method of a class. The class
  should inherit from unittest.TestCase.

  If the API version is less than version, it is expected the test will raise
  a CApiFunctionNotSupportedError exception.

  Parameters
  ----------
  version
    The minimum API version that is required to run the test.
  """

  def decorator(function):
    """Checks if the API version is less than version.

    If API version is less than, an exception is expected to be caught.

    Parameters
    ----------
    function
      The function the decorator is applied to.
    """
    def require_version(self, *args, **kwargs):
      actual_version = Modelling().version
      if actual_version < version:
        with self.assertRaises(CApiFunctionNotSupportedError):
          _ = function(self, *args, **kwargs)

        self.skipTest('Unsupported by current version.')
      else:
        return function(self, *args, **kwargs)

    return require_version

  return decorator


@contextlib.contextmanager
def lower_c_api_version(dll: WrapperBase, lowered_version: tuple[int, int]):
  """Within the with block, lower the C API version reported by the DLL.

  If the C API version is already lower than the given version, no change
  to the API version is made.

  This allows for simulating testing functions against older applications
  which do not have the new functions added in newer C API functions.

  When the with block is exited, the C API version of the DLL is set to
  its original value, even if an error has occurred.

  Parameters
  ----------
  dll
    The DLL to lower the C API version of.
  lowered_version
    The version to lower the C API version of the dll to.
    This must be lower than the version reported by the DLL.

  Notes
  -----
  This only affects code which checks the C API version. For example,
  if the following code was called with the C API version lowered from
  (1, 9) to (1, 8):

  >>> if Modelling().version < (1, 9):
  ...     Modelling().NewFunction(1, 2, 3)
  >>> else:
  ...     Modelling().OldFunction(1, 2)

  Then it would call OldFunction() instead of NewFunction(). Code written like
  this allows for accurate simulation of older API versions by mutating the
  version number.

  However, if the code does not check the API version, then it will still use
  the newer C API. For example, if the following code was called with the C API
  version lowered from (1, 9) to (1, 8):

  >>> try:
  ...     # Added in 1.9
  ...     Modelling().NewFunction(1, 2, 3)
  >>> except AttributeError:
  ...     # Added in 1.2
  ...     Modelling().OldFunction(1, 2)

  Then it will still call NewFunction(). This cannot affect the
  initialisation of the functions available in the C API.
  """
  original_version = dll.version
  try:
    if original_version < lowered_version:
      # The version is already lower then the given version.
      yield
    else:
      dll.version = lowered_version
      yield
  finally:
    dll.version = original_version


def is_testing_against_current_build() -> bool:
  """Return True if testing against an the current build and False otherwise.

  The current build means a build of the source in the repository. Otherwise,
  it will be testing against a pre-made build of an application.
  """
  return 'APPLICATION_BIN' not in os.environ

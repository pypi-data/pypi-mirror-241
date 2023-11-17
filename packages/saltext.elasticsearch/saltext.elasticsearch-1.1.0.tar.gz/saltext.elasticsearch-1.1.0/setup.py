# pylint: disable=missing-module-docstring
import os
import sys

import semantic_release
import setuptools

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass

if __name__ == "__main__":
    module_version = os.environ.get("SALTEXT_ES_MODULE_VERSION", None)
    if module_version is not None:
        setuptools.setup(version=module_version)
    else:
        setuptools.setup(use_scm_version=True)

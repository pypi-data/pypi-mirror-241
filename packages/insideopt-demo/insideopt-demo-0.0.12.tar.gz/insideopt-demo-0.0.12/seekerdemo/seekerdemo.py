import sys
import os
import platform
import importlib.util
import subprocess
import glob


def __bootstrap__():
   global __bootstrap__, __loader__, __file__
   import sys, pkg_resources, imp
   # Get the major and minor Python version
   py_version = f"{sys.version_info.major}{sys.version_info.minor}"
   # Get the operating system
   os_name = platform.system().lower()
   so_file = os.path.join(os.path.dirname(__file__),f"seekerdemo.cpython-310-linux.so")
   spec = importlib.util.spec_from_file_location("seekerdemo", so_file)
   mylib = importlib.util.module_from_spec(spec)
   spec.loader.exec_module(mylib)
   
__bootstrap__()


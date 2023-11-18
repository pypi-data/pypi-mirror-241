import sys
import os
import platform
import importlib.util
import subprocess
import glob


def __bootstrap__():
   global __bootstrap__, __loader__, __file__
   import sys, pkg_resources, imp
   so_file = os.path.join(os.path.dirname(__file__),f"seekerdemo.cpython-310-linux.so")
   spec = importlib.util.spec_from_file_location("seekerdemo", so_file)
   mylib = importlib.util.module_from_spec(spec)
   spec.loader.exec_module(mylib)


def copy_license_to_cwd():
   global __bootstrap__, __loader__, __file__
   import sys, pkg_resources, imp, shutil
   license_file = os.path.join(os.path.dirname(__file__),f"demolicense.sio")
   # Copy the file to the current directory
   shutil.copy(license_file, '.')

   
__bootstrap__()
copy_license_to_cwd()


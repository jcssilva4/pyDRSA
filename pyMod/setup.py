#from distutils.core import setup, Extension
from setuptools import setup, find_packages
from setuptools.extension import Extension

# the c++ extension module: https://docs.python.org/3/distutils/apiref.html#distutils.core.Extension
# for distributions to other platforms: https://docs.python.org/3.3/distutils/builtdist.html

extension_mod = Extension("DRSA",
                            sources = ['DRSAmodule.cpp'],
                            include_dirs=['~/Desktop/DRSA/include'],
                            library_dirs = ['../lib'],
                            language = "c++",
                            extra_objects = ['../lib/libdrsa.a'],
                            #extra_compile_args = ['-fPIC', '-static', '-ldrsa'],
                            #extra_link_args = ['-static']
                            )

setup(name = "Dominance-Based Rough Sets Approach",
      version = '1.0',
      description = 'Decision rule induction from data',
      author = 'Julio C. S. Silva',
      author_email = 'jcss4@cin.ufpe.br',
      url = 'www.greefo.org.br',
      ext_modules = [extension_mod])

# creating built distributions
#https://docs.python.org/3/distutils/builtdist.html
#1)try this https://stackoverflow.com/questions/31380578/how-to-avoid-building-c-library-with-my-python-package
#2)https://docs.python.org/3/library/platform.html
#how to install bdist_wininst linux
#how to pip it -> https://stackoverflow.com/questions/1471994/what-is-setup-py
# 3) also good: https://stackoverflow.com/questions/6292652/what-is-the-difference-between-an-sdist-tar-gz-distribution-and-an-python-egg
# ftp://ftp.ntua.gr/mirror/python/sigs/distutils-sig/doc/sc_submission.html
# https://news.ycombinator.com/item?id=12285497
# https://stackoverflow.com/questions/39776911/how-to-compile-cython-module-for-multiple-platforms-on-windows

#APPVEYOR: https://packaging.python.org/guides/supporting-windows-using-appveyor/

'''
https://stackoverflow.com/questions/50281252/python-wheel-packages-linux-vs-windows
The most common reason for a package to be platform-specific is that it includes C API extension modules,
 as is the case with numpy. But there can be other reasons. For example, it may include a native executable 
 to subprocess, or it may use ctypes to access system APIs, etc.
'''

# https://stackoverflow.com/questions/51805034/portable-python-c-api-build-with-cmake
# binary distribution python c api portable

'''
check this link:
https://packaging.python.org/guides/packaging-binary-extensions/#use-cases
go to additional resources topic and then: https://scikit-build.readthedocs.io/en/latest/generators.html
'''

'''
According to https://docs.python.org/3/distutils/builtdist.html , distutils only
 supports cross-compiling between win32 and win_amd64 as of this writing (3.7).
Moreover, building extensions with compilers other than the MSVC that Python is built 
with is not officially supported.

It is theoretically possible by getting a Linux toolchain for win32/64 (including the
necessary headers and link libraries), a set of the necessary Python for Windows binaries to 
link against, then forge compiler and linker paths and/or options in setup.py -- though it
will still be an unsupported setup.

So you'll be better off using a Windows VM or an online build service like AppVeyor.

'''

'''
NEW
https://stackoverflow.com/questions/48518055/cross-compile-extension-on-linux-for-windows
'''

#CMake: https://martinopilia.com/posts/2018/09/15/building-python-extension.html

# WHEELS
# https://stackoverflow.com/questions/26059111/build-a-wheel-egg-and-all-dependencies-for-a-python-project
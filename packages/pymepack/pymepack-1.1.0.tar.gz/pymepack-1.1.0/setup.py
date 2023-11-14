from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import configparser
import os.path
import numpy
import sys



if sys.version_info.major != 3:
    error("Only Python 3 is supported.")

# Default libary Names
mepack_lib_name = 'mepack'
blas_lib_name = 'blas'
lapack_lib_name = 'lapack'
library_dirs = list()

# Load Config
if os.path.exists('./pymepack.cfg'):
    config = configparser.ConfigParser()
    config.read('./pymepack.cfg')
    if config.has_option('build','library_dirs'):
        l = config.get('build', 'library_dirs').split(',')
        for ld in l:
            if len(ld.strip()) > 0:
                library_dirs.append(ld)
    if config.has_option('build','mepack'):
        mepack_lib_name = config.get('build', 'mepack')
    if config.has_option('build','blas'):
        blas_lib_name = config.get('build', 'blas')
    if config.has_option('build','lapack'):
        lapack_lib_name =config.get('build', 'lapack')



# Extensions

pymepack_impl = Extension(
        name = 'pymepack.pymepack_impl',
        sources = ['./pymepack/pymepack_impl.pyx'],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        include_dirs=['./pymepack']
      )

pymepack_impl.libraries=[mepack_lib_name, lapack_lib_name, blas_lib_name]

for d in library_dirs:
    pymepack_impl.library_dirs.append(d)
    pymepack_impl.runtime_library_dirs.append(d)

pymepack_impl.include_dirs.insert(0,numpy.get_include())


lapack_sources = []
bench_sources = [
        './pymepack/generator/BB03AD.c',
        './pymepack/generator/BB04AD.c',
        './pymepack/generator/f2c_helper.c'
        ]

if sys.version_info.minor <= 10:
    bench_sources.extend([
            './pymepack/generator/py37/benchmarksmodule.c',
            './pymepack/generator/py37/fortranobject.c'
        ])
    lapack_sources.extend([
            './pymepack/lapack/py37/lapackmodule.c',
            './pymepack/lapack/py37/fortranobject.c'
        ])

if sys.version_info.minor >= 11:
    bench_sources.extend([
            './pymepack/generator/py311/benchmarksmodule.c',
            './pymepack/generator/py311/fortranobject.c'
        ])
    lapack_sources.extend([
            './pymepack/lapack/py311/lapackmodule.c',
            './pymepack/lapack/py311/fortranobject.c'
        ])

bench = Extension(
            name='pymepack.generator.benchmarks',
            sources=bench_sources )

bench.include_dirs.insert(0,numpy.get_include())
bench.libraries = [ lapack_lib_name, blas_lib_name ]

lapack = Extension(
            name='pymepack.lapack.lapack',
            sources=lapack_sources )
lapack.include_dirs.insert(0,numpy.get_include())
lapack.libraries = [ lapack_lib_name, blas_lib_name ]

for d in library_dirs:
    bench.library_dirs.append(d)
    bench.runtime_library_dirs.append(d)
    lapack.library_dirs.append(d)
    lapack.runtime_library_dirs.append(d)

exts = [ pymepack_impl, bench, lapack]

setup(
      name="pymepack",
      include_package_data=False,
      package_data = {"pymepack": ["*.pxd"]},
#      packages=["pymepack",
#                "pymepack.generator",
#                "pymepack.tests"],
      packages = find_packages(where='.', exclude = ['pymepack.generator.py311',
          'pymepack.lapack.py37',
          'pymepack.lapack.py311',
          'pymepack.generator.py37']),
      ext_modules = cythonize( exts,
                               compiler_directives={'language_level' : "3"},
                               include_path=["pymepack"])

      )


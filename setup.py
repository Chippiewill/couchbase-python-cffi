from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install

# Use a function to defer the import in case the
# cffi/couchbase packages aren't installed.
def get_ext_modules():
    import couchbase_ffi._cinit
    return [couchbase_ffi._cinit.ffi.verifier.get_extension()]

class CFFIBuild(build_ext):
    def finalize_options(self):
        self.distribution.ext_modules = get_ext_modules()
        build.finalize_options(self)

class CFFIInstall(install):
    def finalize_options(self):
        self.distribution.ext_modules = get_ext_modules()
        install.finalize_options(self)

setup_args = {
    'zip_safe': False,
    'author': "Mark Nunberg",
    'author_email': "mnunberg@haskalah.org",
    'license': "Apache License 2.0",
    'description': "Couchbase Client API using CFFI",
    'keywords': ["PyPy", "nosql", "pycouchbase", "libcouchbase", "couchbase"],
    'install_requires': ['cffi', 'couchbase==2.0.7'],
    'tests_require': ['nose', 'testresources'],
    'setup_requires': ["cffi", "couchbase==2.0.7"],
    'cmdclass': {
        "build_ext": CFFIBuild,
        "install": CFFIInstall,
    },
    'classifiers': [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython"
    ],

    'packages': ['couchbase_ffi'],
    'package_data': {'couchbase_ffi':['_lcb.h']},
    'name': 'couchbase_ffi',
    'version': '0.2.0.0',
    'url': 'https://github.com/couchbaselabs/couchbase-python-cffi'
}

setup(**setup_args)

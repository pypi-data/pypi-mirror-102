#!/usr/bin/env python
###########################
# This code block is a HACK (!), but is necessary to avoid code duplication. Do NOT alter these lines.
import os
from setuptools import setup
import importlib.util
filepath = os.path.abspath(os.path.dirname(__file__))
filepath_import = os.path.join(filepath, '..', 'core', 'src', 'autogluon', 'core', '_setup_utils.py')
spec = importlib.util.spec_from_file_location("ag_min_dependencies", filepath_import)
ag = importlib.util.module_from_spec(spec)
# Identical to `from autogluon.core import _setup_utils as ag`, but works without `autogluon.core` being installed.
spec.loader.exec_module(ag)
###########################

version = ag.load_version_file()
version = ag.update_version(version)

submodule = 'tabular'
requirements = [
    # version ranges added in ag.get_dependency_version_ranges()
    'numpy',
    'scipy',
    'pandas',
    'scikit-learn',

    'psutil>=5.0.0,<=5.7.0',  # TODO: psutil 5.7.1/5.7.2 has non-deterministic error on CI doc build -  ImportError: cannot import name '_psutil_linux' from 'psutil'
    'networkx>=2.3,<3.0',
    f'autogluon.core=={version}',
    f'autogluon.features=={version}',
]

test_requirements = [
    'pytest',
]

extras_require = {
    'lightgbm': [
        'lightgbm>=3.0,<4.0',
    ],
    'catboost': [
        'catboost>=0.23.0,<0.25',
    ],
    'xgboost': [
        'xgboost>=1.3.2,<1.4',
    ],
    'fastai': [
        'torch>=1.0,<2.0',
        'fastai>=2.0,<3.0',
    ],
}

all_requires = []
for extra_package in ['lightgbm', 'catboost', 'xgboost', 'fastai']:
    all_requires += extras_require[extra_package]
all_requires = list(set(all_requires))
extras_require['all'] = all_requires

install_requires = requirements + test_requirements
install_requires = ag.get_dependency_version_ranges(install_requires)

if __name__ == '__main__':
    ag.create_version_file(version=version, submodule=submodule)
    setup_args = ag.default_setup_args(version=version, submodule=submodule)
    setup(
        install_requires=install_requires,
        extras_require=extras_require,
        **setup_args,
    )

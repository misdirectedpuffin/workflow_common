"""Package setup file."""

import os

try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

from setuptools import find_packages, setup


def get_version():
    """Return the current version."""
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(curr_dir, 'version.txt')) as version_file:
        return version_file.read().strip()


def get_requirements(file):
    """Return a list of requirements from a file."""
    requirements = parse_requirements(file, session=False)
    return [str(ir.req) for ir in requirements if not None]


setup(
    name="workflow_common",
    version=get_version(),
    url="https://github.com/misdirectedpuffin/workflow-common",
    author="misdirectedpuffin",
    author_email="misdirectedpuffin@gmail.com",
    description="common lib for workflow plugins",
    long_description=open('README.rst').read(),
    packages=find_packages(),
    install_requires=['pytest-runner'],
    tests_require=get_requirements('requirements_dev.txt'),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

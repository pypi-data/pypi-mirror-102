import sys
from setuptools import setup, find_packages

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)
REQUIREMENTS = []

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
    ==========================
    Unsupported python version
    ==========================
    This version of drf-condition-serializers required Python must be {}.{} or newer
    """.format(*REQUIRED_PYTHON))


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    pass


setup(
    name='drf-condition-serializers',
    version='0.1.1',
    url='https://github.com/Zomba4okk/DRFConditionSerializers',
    download_url='https://github.com/Zomba4okk/DRFConditionSerializers/archive/refs/tags/v_011.tar.gz',
    license='MIT',
    description='',
    long_description=read('README.md'),
    author='Anton Zagrebancev',
    author_email='anton.zagrebancev@gmail.com',
    packages=find_packages(exclude=['test*']),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    python_requires=">=3.5",
    zip_safe=False,
    project_urls={}
)
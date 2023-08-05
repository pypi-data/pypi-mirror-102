"""neuror setup.py"""
import imp
import sys

from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    sys.exit("Sorry, Python < 3.6 is not supported")

# read the contents of the README file
with open("README.rst", encoding='utf-8') as f:
    README = f.read()

setup(
    name='NeuroR',
    author='Blue Brain Project, EPFL',
    description='A morphology repair tool',
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/bluebrain/neuror",
    license="LGPLv3",
    install_requires=[
        'click>=0.7.0',
        'matplotlib>=2.2.3',
        'morph-tool>=0.1.14',
        'morphio>=2.1.1',
        'neurom>=2.0.0.dev0',
        'numpy>=1.19.2',
        'nptyping>=1.3.0',
        'pandas>=0.24.2',
        'pyquaternion>=0.9.2',
        'scipy>=1.2.0',
    ],
    extras_require={
        'plotly': [
            'dash-core-components>=0.46.0',  # HTML components
            'dash-table>=3.6.0',  # Interactive DataTable component (new!)
            'dash>=0.41.0',  # The core dash backend
            'plotly-helper>=0.0.2',
        ],
        'docs': [
            'sphinx-autorun>=1.1.1',
            'sphinx-bluebrain-theme>=0.2.4',
            'sphinx-click>=2.5.0',
            'sphinx>=2.0.0',
        ],
    },
    packages=find_packages(),
    entry_points={'console_scripts': ['neuror=neuror.cli:cli']},
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)

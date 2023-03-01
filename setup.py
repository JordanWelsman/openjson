# Module imports
from setuptools import setup

# Arguments
version = "0.0.0" # update __init__.py
python_version = ">=3.10"

# Long description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

# modular-json package data
py_modules = ["load", "save"]

# Run setup function
setup(
    name='modular-json',
    version=version,
    description='A modular approach to handling JSON.',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jordan Welsman',
    author_email='jordan.welsman@outlook.com',
    url='https://pypi.org/project/modular-json/',
    download_url='https://github.com/JordanWelsman/modular-json/tags',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ],
    package_data = {
      'modular-json': py_modules
      },
    python_requires=python_version,
    keywords='python, json, modular, parsing, interpreting, exporting, importing'
)
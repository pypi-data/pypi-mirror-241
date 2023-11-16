from setuptools import setup

name = "types-hdbcli"
description = "Typing stubs for hdbcli"
long_description = '''
## Typing stubs for hdbcli

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the `hdbcli` package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`hdbcli`.

This version of `types-hdbcli` aims to provide accurate annotations
for `hdbcli==2.18.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/hdbcli. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `4aae235cefd62ec417b92166d2bcf038cb8801e8` and was tested
with mypy 1.7.0, pyright 1.1.334, and
pytype 2023.10.31.
'''.lstrip()

setup(name=name,
      version="2.18.0.1",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/hdbcli.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['hdbcli-stubs'],
      package_data={'hdbcli-stubs': ['__init__.pyi', 'dbapi.pyi', 'resultrow.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      python_requires=">=3.7",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)

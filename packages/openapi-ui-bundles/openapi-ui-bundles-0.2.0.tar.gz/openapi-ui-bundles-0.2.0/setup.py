#!/usr/bin/env python

import pathlib
from setuptools import setup, find_packages

requirements = [
]


with open('README.rst', 'r') as file:
    readme = file.read()


def parse_about():
    about_globals = {}
    this_path = pathlib.Path(__file__).parent
    about_module_text = pathlib.Path(this_path, 'openapi_ui_bundles', '__about__.py').read_text()
    exec(about_module_text, about_globals)

    return about_globals


about = parse_about()


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    author=about['__author__'],
    author_email=about['__email__'],
    url=about['__url__'],
    license=about['__license__'],
    keywords=[
        'documentation ',
        'api-documentation',
        'api-schema',
        'swagger',
        'swagger-ui',
        'swagger-documentation',
        'swagger-specification',
        'openapi',
        'openapi-ui',
        'openapi-specification',
        'openapi-documentation',
        'redoc',
        'rapidoc',
    ],
    python_requires=">=3.5",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    project_urls={
        'Source': 'https://github.com/dapper91/python-openapi_ui_bundles',
    },
    include_package_data=True,
)

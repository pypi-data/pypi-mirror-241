"""
ReDoc static files. See https://github.com/Redocly/redoc.
"""

import pathlib

__all__ = ['static_path']

this_path = pathlib.Path(__file__).parent
static_path = this_path / 'vendor'

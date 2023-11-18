"""
Swagger UI 3.X static files. See https://github.com/swagger-api/swagger-ui.
"""

import pathlib

__all__ = ['static_path']

this_path = pathlib.Path(__file__).parent
static_path = this_path / 'vendor'

Python OpenAPI UI bundles
=========================

This package provides the static files for `OpenAPI <https://swagger.io/specification/>`_ UI tools as a python package.
The following UI tools are included:

- `Swagger UI <https://github.com/swagger-api/swagger-ui>`_.
- `RapiDoc <https://github.com/mrin9/RapiDoc>`_.
- `ReDoc <https://github.com/Redocly/redoc>`_.


Flask usage example:
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import flask
    import openapi_ui_bundles

    app = flask.Flask(__name__, static_folder=openapi_ui_bundles.swagger_ui.static_path, static_url_path='/')

    if __name__ == "__main__":
        app.run()


Swagger UI
----------

.. image:: images/swagger-ui-screenshot.png
  :width: 1024
  :alt: Swagger UI example


RapiDoc
-------

.. image:: images/rapidoc-screenshot.png
  :width: 1024
  :alt: RapiDoc UI example


ReDoc
-----

.. image:: images/redoc-screenshot.png
  :width: 1024
  :alt: ReDoc UI example
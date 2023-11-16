====================
Django Zupit Logging
====================

A Django Middleware for logging requests and responses accordingly to Zupit Standards.

Installation
------------
Install using ``pip``::

    pip install django_zupit_logging

Configuration
-------------

Add ``django_zupit_logging`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = [
        ...
        'django_zupit_logging',
    ]

Add ``django_zupit_logging.middleware.ZupitLoggingMiddleware`` to your ``MIDDLEWARE`` setting::

        MIDDLEWARE = [
            ...
            'django_zupit_logging.middleware.ZupitLoggingMiddleware',
        ]

Add ``ZUPIT_LOGGING`` to your ``settings.py`` file::

    ZUPIT_LOGGING = {
        "APP_INSIGHTS_CONNECTION_STRING": env("APP_INSIGHTS_CONNECTION_STRING"),
    }

Use ``enable_zupit_logger(LOGGING)`` to your ``settings.py`` file::

        from django_zupit_logging.settings import enable_zupit_logger

        if env("APP_INSIGHTS_CONNECTION_STRING"):
            enable_zupit_logger(LOGGING)


Usage
-----

The middleware will log requests and responses accordingly to Zupit Standards.

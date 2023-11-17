#!/usr/bin/env python
# -*- coding: utf8 -*-
from __future__ import (
    absolute_import,
    division,
    generators,
    nested_scopes,
    print_function,
    unicode_literals,
    with_statement,
)
from zenutils.logutils import *
from zenutils.logutils import get_simple_config as get_simple_config_core

"""
Make logging setup easy. Default logging settings:

```
logging_config = {
   "version": 1,
   "disable_existing_loggers": False,
   "formatters": {
      "default": {
            "format": "{asctime} {levelname} {pathname} {lineno} {module} {funcName} {process} {thread} {message}",
            "style": "{"
      },
      "message_only": {
            "format": "{message}",
            "style": "{",
      },
      "json": {
            "class": "jsonformatter.JsonFormatter",
            "format": {
               "asctime": "asctime",
               "levelname": "levelname",
               "pathname": "pathname",
               "lineno": "lineno",
               "module": "module",
               "funcName": "funcName",
               "process": "process",
               "thread": "thread",
               "message": "message",
            },
      },
   },
   "handlers": {
      "default_console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "default",
      },
      "default_file": {
            "level": "DEBUG",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": logfile,
            "when": "midnight",
            "interval": 1,
            "backupCount": 30,
            "formatter": "default",
      },
      "json_console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "json",
      },
      "json_file": {
            "level": "DEBUG",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": logfile,
            "when": "midnight",
            "interval": 1,
            "backupCount": 30,
            "formatter": "json",
      },
   },
   "loggers": {
   },
   "root": {
      "handlers": ["default_file", "default_console"],
      "level": loglevel,
      "propagate": True,
   }
}
```

Example:

```
from fastutils import logutils

def setup(settings):
    logging_settings = settings.get("logging", {})
    logutils.setup(**logging_settings)

```
"""

import zenutils.logutils

__all__ = [] + zenutils.logutils.__all__

from jsonformatter import JsonFormatter


def get_simple_config(
    logfile=None,
    loglevel=None,
    logfmt=None,
    loggers=None,
    logging=None,
    console_handler_class=None,
    file_handler_class=None,
    **kwargs
):
    """Make simple logging settings.

    logfile default to app.log.
    loglevel choices are: DEBUG/INFO/WARNING/ERROR. default to INFO.
    logfmt choices are: default/message_only/json. default to default.
    Use logger parameter to override the default settings' logger sections.
    Use logging parameter to override the whole settings.

    """
    from zenutils import dictutils

    # default logging template
    logging_config = {
        "formatters": {
            "json": {
                "class": ".".join([JsonFormatter.__module__, JsonFormatter.__name__]),
                "format": {
                    "asctime": "asctime",
                    "levelname": "levelname",
                    "pathname": "pathname",
                    "lineno": "lineno",
                    "module": "module",
                    "funcName": "funcName",
                    "process": "process",
                    "thread": "thread",
                    "message": "message",
                },
            },
            "simple_json": {
                "class": ".".join([JsonFormatter.__module__, JsonFormatter.__name__]),
                "format": {
                    "asctime": "asctime",
                    "levelname": "levelname",
                    "message": "message",
                },
            },
        },
        "handlers": {
            "json_console": get_console_handler(
                "json", "DEBUG", handler_class=console_handler_class
            ),
            "json_file": get_file_handler(
                logfile, "json", "DEBUG", handler_class=file_handler_class
            ),
            "simple_json_console": get_console_handler(
                "simple_json", "DEBUG", handler_class=console_handler_class
            ),
            "simple_json_file": get_file_handler(
                logfile, "simple_json", "DEBUG", handler_class=file_handler_class
            ),
        },
    }
    dictutils.deep_merge(
        logging_config,
        get_simple_config_core(
            logfile,
            loglevel,
            logfmt,
            loggers,
            logging,
            console_handler_class,
            file_handler_class,
            **kwargs
        ),
    )
    return logging_config

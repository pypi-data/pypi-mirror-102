__title__ = 'botdash.pro'
__author__ = 'Seer#6054'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020-2021 Seer-software'
__version__ = '0.0.1'

from .client import Client
from .lib.util import objects, exceptions
from requests import get
from json import loads

# __newest__ = loads(get("https://pypi.python.org/pypi/botdash.pro/json").text)["info"]["version"]

# if __version__ != __newest__:
#     print(exceptions.LibraryUpdateAvailable(f"New version available for {__title__}: '{__newest__}' (Using: '{__version__}')\nGet latest here: https://pypi.python.org/pypi/botdash.pro\nInstall command: 'pip install botdash.pro=={__newest__}'"))

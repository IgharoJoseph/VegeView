import os
from pathlib import Path
from split_settings.tools import include
from decouple import config

include(
    'base.py'
)
import sys
from os import path
from pathlib import Path
import re
from . import wavtotext

urlpatterns = [
    path('', wavtotext.filename(), name='home'),
]
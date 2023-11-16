import re
import pathlib

from .wss import WSClient, Intents
from .abc import Embed, Color, Activity

Client = WSClient
Intents = Intents()
Color = Color()
Activity = Activity()

def set_tkrdisc_info():
  __name__ = 'tkrdisc'
  __version__ = '0.2.8.1'
  __author__ = 'tlkr.'
  __license__ = 'MIT'
  __author_email__ = 'toolkitr.email@gmail.com'
  __description__ = 'Custom Discord API Wrapper'
  __url__ = 'https://github.com/toolkitr/tkrdisc'

set_tkrdisc_info()
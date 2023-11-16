import re

from .wss import WSClient, Intents
from .abc import Embed, Color, Activity

Client = WSClient
Intents = Intents()
Color = Color()
Activity = Activity()

def set_tkrdisc_info():
  with open('toolkitr/tkrdisc/setup.cfg', 'r') as file:
      config_data = file.read()

  metadata_pattern = r'\[metadata\]\s*(.*?)\s*\[|\Z'
  options_pattern = r'\[options\]\s*(.*?)\s*\[|\Z'
  key_value_pattern = r'([\w_]+)\s*=\s*(.*)'

  metadata_matches = re.findall(metadata_pattern, config_data, re.DOTALL)
  metadata_data = '\n'.join(metadata_matches)
  metadata_pairs = re.findall(key_value_pattern, metadata_data)

  options_matches = re.findall(options_pattern, config_data, re.DOTALL)
  options_data = '\n'.join(options_matches)
  options_pairs = re.findall(key_value_pattern, options_data)

  globals().update({f'__{key.strip()}__': value.strip() for key, value in metadata_pairs})
  globals().update({f'__{key.strip()}__': value.strip() for key, value in options_pairs})

set_tkrdisc_info()
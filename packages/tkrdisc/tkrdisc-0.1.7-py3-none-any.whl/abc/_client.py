import asyncio

class Client:
    def __init__(self, id: int, name: str, prefix: str, intents: int, help_command: bool):
      self.id = id
      self.name = name
      self.prefix = prefix
      self.intents = intents
      self.help_command = help_command
      self.session = None
      self.token = None
      self.wss = "wss://gateway.discord.gg/?v=9&encoding=json"
      self.session_id = int

      self.commands = {}
      self.events = {}
      self.aliases = {}
      self.command_aliases = {}
      self.command_desc = {}

    def __repr__(self):
      return str(self.name)

    def __str__(self):
      return self.__repr__()

    def command(self, aliases: list=[], description: str = ""):
      def wrapper(func, *args, **kwargs):
        self.commands[f'{self.prefix}{func.__name__}'] = func
        for alias in aliases: self.aliases[f'{self.prefix}{alias}'] = func
        self.command_aliases[f'{self.prefix}{func.__name__}'] = [f'{self.prefix}{alias}' for alias in aliases]
        self.command_desc[f'{self.prefix}{func.__name__}'] = description
      return wrapper

    def event(self):
      def wrapper(func, *args, **kwargs):
        self.events[str(func.__name__)] = func
      return wrapper

    def register(self, func, aliases: list=[], description: str = ""):
      self.commands[f'{self.prefix}{func.__name__}'] = func
      for alias in aliases: self.aliases[f'{self.prefix}{alias}'] = func
      self.command_aliases[f'{self.prefix}{func.__name__}'] = [f'{self.prefix}{alias}' for alias in aliases]
      self.command_desc[f'{self.prefix}{func.__name__}'] = description

    def _login(self, token):
      self.token = token
      return {
          "op": 2,
          "d": {
              "token": token,
              "intents": self.intents,  
              "properties": {
                  "$os": "linux",
                  "$browser": "disctool",
                  "$device": "disctool"
              }
          }
      }
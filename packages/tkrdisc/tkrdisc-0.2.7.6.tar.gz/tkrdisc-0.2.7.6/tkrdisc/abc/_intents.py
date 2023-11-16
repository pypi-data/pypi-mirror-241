class Intents:
  def __init__(self):
      self.intents = 0
      self.valid_intents = ['GUILDS', 'GUILD_MEMBERS', 'GUILD_BANS', 'GUILD_EMOJIS',
                            'GUILD_INTEGRATIONS', 'GUILD_WEBHOOKS', 'GUILD_INVITES',
                            'GUILD_VOICE_STATES', 'GUILD_PRESENCES', 'GUILD_MESSAGES',
                            'GUILD_MESSAGE_REACTIONS', 'GUILD_MESSAGE_TYPING',
                            'DIRECT_MESSAGES', 'DIRECT_MESSAGE_REACTIONS', 'DIRECT_MESSAGE_TYPING']

  def __setattr__(self, name, value):
      if name == 'intents':
          self.__validate_intents(value)
      super().__setattr__(name, value)

  def __getattr__(self, name):
      if name == 'intents':
          return self.intents
      raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

  def __repr__(self):
      return f"<Intents intents={self.intents}>"

  def __str__(self):
      return self.__repr__()

  def get_valid_intents(self):
      return self.valid_intents

  def all(self):
      self.intents = (1 << len(self.valid_intents)) - 1
      return self.intents

  def __validate_intents(self, value):
      if isinstance(value, int):
        super().__setattr__('intents', value)
      elif isinstance(value, list):
          self.intents = 0
          for intent in value:
              if intent in self.valid_intents:
                  self.intents |= 1 << self.valid_intents.index(intent)
              else:
                  raise ValueError(f"Invalid intent: {intent}")
      else:
          raise TypeError("Intents must be an integer or a list of valid intents")
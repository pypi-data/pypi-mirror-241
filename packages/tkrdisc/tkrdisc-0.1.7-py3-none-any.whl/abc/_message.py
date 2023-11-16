from ._user import User
from ._guild import Guild
from ._channel import Channel

class Message:
  def __init__(self, context, token):
    self.id = context.get('id')
    self.is_slash_command = False
    self.type = context.get('type')
    self.tts = context.get('tts')
    self.timestamp = context.get('timestamp')
    self.referenced_message = context.get('referenced_message')
    self.pinned = context.get('pinned')
    self.nonce = context.get('nonce')
    self.mentions = context.get('mentions')
    self.mention_roles = context.get('mention_roles')
    self.mention_everyone = context.get('mention_everyone')
    self.message_id = context.get('id')
    self.flags = context.get('flags')
    self.embeds = context.get('embeds')
    self.edited_timestamp = context.get('edited_timestamp')
    self.content = context.get('content')
    self.components = context.get('components')
    self.attachments = context.get('attachments')
    if context.get('channel_id'): self.channel = Channel(context.get('channel_id'), token)
    if context.get('guild_id'): self.guild = Guild(context.get('guild_id'), token)

    try: self.author = User(context.get('author').get('id'), token)
    except: self.author = None
import aiohttp
import asyncio
import datetime

from ..abc import (
      Client,
      Intents,
      Embed,
      Color
)
from .wsevent import WSEvent

from ..core import ObjectSearch

class WSClient:
    def __init__(self, id: int, name: str, prefix: str, intents: int, help_command: bool):
      self.client = Client(id, name, prefix, intents, help_command)
      if help_command == True: self.client.register(self.help)
      self.command_aliases = self.client.command_aliases
      self.command = self.client.command
      self.event = self.client.event
      self.ws = None
      self.session_id = int
      self.id = self.client.id
      self.name = self.client.name
      self.prefix = self.client.prefix
      self.intents = self.client.intents

      self.searcher = None

    async def help(self, ctx):
      cmd_aliases = ''
      for cmd in self.client.command_aliases:
        add_on = f'{cmd}'
        if len(self.client.command_aliases[cmd]) > 0:
          add_on += f' -> ({", ".join(self.client.command_aliases[cmd])})'

        add_on = f'> {add_on}'
        if self.client.command_desc.get(cmd) != "":
          add_on += f'  >  `{self.client.command_desc[cmd]}`'
        cmd_aliases += f'{add_on}\n'    

      embed = Embed(title =f"{str(self.client)}'s Commands:", description=f'{cmd_aliases}', color = Color().random())
      await ctx.send(embed=embed())

    def get_channel(self, channel_id):
      channel_data = self.searcher.search_channel(channel_id)
      return channel_data

    def get_guild(self, guild_id):
      guild_data = self.searcher.search_guild(guild_id)
      return guild_data

    def get_user(self, user_id):
      user_data = self.searcher.search_user(user_id)
      return user_data

    async def start(self, token):
      self.searcher = ObjectSearch(token)
      async with aiohttp.ClientSession() as session:
        async with session.ws_connect(self.client.wss) as ws:
          self.ws = ws
          await ws.send_json(self.client._login(token))

          async for message in ws:
            await WSEvent(message, self).process_op()

    async def latency(self):
      start_time = datetime.datetime.now()
      await self.ws.ping()
      end_time = datetime.datetime.now()
      latency = (end_time - start_time).total_seconds() * 1000
      return str(round(latency*1000))

    async def close(self):
      await self.ws.close()

    def run(self, token): 
      asyncio.run(self.start(token))

    async def set_presence(self, activity, type=0):
      payload = {
          "op": 3,
          "d": {
              "since": None,
              "activities": [
                  {
                      "name": activity,
                      "type": type
                  }
              ],
              "status": "online",
              "afk": False
          }
      }
      await self.ws.send_json(payload)

    def __str__(self):
      return self.client.name
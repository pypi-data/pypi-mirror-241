import requests
import json

class User:
  def __init__(self, user_id, token):
    self.token = token

    self._user_dict = self._get_info(user_id)
    self.id = self._user_dict.get('id')
    self.username = self._user_dict.get('username')
    self.avatar = f'https://cdn.discordapp.com/avatars/{self.id}/{self._user_dict.get("avatar")}.png?size=4096'
    self.discriminator = self._user_dict.get('discriminator')
    self.public_flags = self._user_dict.get('public_flags')
    self.premium_type = self._user_dict.get('premium_type')
    self.flags = self._user_dict.get('flags')
    self.banner = self._user_dict.get('banner')
    self.accent_color = self._user_dict.get('accent_color')
    self.global_name = self._user_dict.get('global_name')
    self.nickname = self.global_name
    self.nick = self.nickname
    self.avatar_decooration_data = self._user_dict.get('avatar_decoration_data')
    self.banner_color = self._user_dict.get('banner_color')

    self.roles = []
    self.joined_at = None
    self.deaf = False
    self.communication_disabled_until = None
    self.pending = False

  def _get_info(self, user_id):
    headers = {
        'Authorization': f'Bot {self.token}'
    }

    response = requests.get(f'https://discord.com/api/v9/users/{user_id}', headers=headers)
    user_data = response.json()
    return user_data
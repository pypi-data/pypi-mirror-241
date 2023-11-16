import requests
import json

class Bot:
  def __init__(self, token):
    self.token = token

    self._user_dict = self._get_info()
    self.id = self._user_dict.get('id')
    self.username = self._user_dict.get('username')
    self.avatar = self._user_dict.get('avatar')
    self.discriminator = self._user_dict.get('discriminator')
    self.public_flags = self._user_dict.get('public_flags')
    self.premium_type = self._user_dict.get('premium_type')
    self.flags = self._user_dict.get('flags')
    self.bot = self._user_dict.get('bot')
    self.banner = self._user_dict.get('banner')
    self.accent_color = self._user_dict.get('accent_color')
    self.global_name = self._user_dict.get('global_name')
    self.avatar_decoration_data = self._user_dict.get('avatar_decoration_data')
    self.banner_color = self._user_dict.get('banner_color')
    self.mfa_enabled = self._user_dict.get('mfa_enabled')
    self.locale = self._user_dict.get('locale')
    self.email = self._user_dict.get('email')
    self.verified = self._user_dict.get('verified')
    self.bio = self._user_dict.get('bio')

  def _get_info(self):
    headers = {
        'Authorization': f'Bot {self.token}'
    }

    response = requests.get(f'https://discord.com/api/v9/users/@me', headers=headers)
    user_data = response.json()
    return user_data
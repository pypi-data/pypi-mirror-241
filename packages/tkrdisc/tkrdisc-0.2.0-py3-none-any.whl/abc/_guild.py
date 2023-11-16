import requests
import json

from ._user import User
from ._role import Role
from ._channel import Channel

class Guild:
  def __init__(self, guild_id, token):
    self.token = token

    self._guild_dict = self._get_info(guild_id)
    self.id = self._guild_dict.get('id')
    self.name = self._guild_dict.get('name')
    self.icon = self._guild_dict.get('icon')
    self.owner_id = self._guild_dict.get('owner_id')
    self.owner = User(self.owner_id, self.token)
    self.permissions = self._guild_dict.get('permissions')
    self.features = self._guild_dict.get('features')
    self.emojis = self._guild_dict.get('emojis')
    self.roles = [Role(role) for role in self._guild_dict.get('roles')]
    self.channels = self._set_channels()
    self.members = self._guild_dict.get('members')
    self.presences = self._guild_dict.get('presences')
    self.voice_states = self._guild_dict.get('voice_states')
    self.threads = self._guild_dict.get('threads')
    self.stage_instances = self._guild_dict.get('stage_instances')
    self.thread_member_lists = self._guild_dict.get('thread_member_lists')
    self.thread_metadata = self._guild_dict.get('thread_metadata')
    self.stickers = self._guild_dict.get('stickers')
    self.bans = self._guild_dict.get('bans')
    self.integrations = self._guild_dict.get('integrations')
    self.widget = self._guild_dict.get('widget')
    self.widget_enabled = self._guild_dict.get('widget_enabled')
    self.widget_channel_id = self._guild_dict.get('widget_channel_id')
    self.nsfw_level = self._guild_dict.get('nsfw_level')
    self.nsfw = self._guild_dict.get('nsfw')
    self.description = self._guild_dict.get('description')
    self.banner = self._guild_dict.get('banner')
    self.splash = self._guild_dict.get('splash')
    self.discovery_splash = self._guild_dict.get('discovery_splash')
    self.emoji_limit = self._guild_dict.get('emoji_limit')
    self.roles_limit = self._guild_dict.get('roles_limit')
    self.channels_limit = self._guild_dict.get('channels_limit')
    self.bitrate_limit = self._guild_dict.get('bitrate_limit')
    self.member_limit = self._guild_dict.get('member_limit')
    self.premium_subscription_count = self._guild_dict.get('premium_subscription_count')
    self.premium_progress_bar_enabled = self._guild_dict.get('premium_progress_bar_enabled')
    self.application_id = self._guild_dict.get('application_id')
    self.system_channel_id = self._guild_dict.get('system_channel_id')
    self.system_channel_flags = self._guild_dict.get('system_channel_flags')
    self.rules_channel_id = self._guild_dict.get('rules_channel_id')
    self.public_updates_channel_id = self._guild_dict.get('public_updates_channel_id')
    self.preferred_locale = self._guild_dict.get('preferred_locale')
    self.premium_tier = self._guild_dict.get('premium_tier')
    self.premium_guild_subscription_count = self._guild_dict.get('premium_guild_subscription_count')
    self.joined_at = self._guild_dict.get('joined_at')
    self.large = self._guild_dict.get('large')
    self.unavailable = self._guild_dict.get('unavailable')
    self.member_count = self._guild_dict.get('member_count')
    self.voice_states_count = self._guild_dict.get('voice_states_count')
    self.presences_count = self._guild_dict.get('presences_count')
    self.max_presences = self._guild_dict.get('max_presences')
    self.max_members = self._guild_dict.get('max_members')
    self.vanity_url_code = self._guild_dict.get('vanity_url_code')


  def _get_info(self, guild_id):
    headers = {
        'Authorization': f'Bot {self.token}'
    }

    response = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}', headers=headers)
    user_data = response.json()
    return user_data

  def _set_channels(self):
    headers = {
        'Authorization': f'Bot {self.token}'
    }

    response = requests.get(f'https://discord.com/api/v9/guilds/{self.id}/channels', headers=headers)
    user_data = response.json()
    return user_data
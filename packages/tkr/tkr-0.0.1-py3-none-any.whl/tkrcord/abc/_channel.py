import requests
import json


class Channel:
  def __init__(self, channel_id, token):
    self.token = token

    self._channel_dict = self._get_info(channel_id)
    self.id = self._channel_dict.get('id')
    self.type = self._channel_dict.get('type')
    self.flags = self._channel_dict.get('flags')
    self.name = self._channel_dict.get('name')
    self.parent_id = self._channel_dict.get('parent_id')
    self.topic = self._channel_dict.get('topic')
    self.position = self._channel_dict.get('position')
    self.permission_overwrites = self._channel_dict.get('permission_overwrites')    

  def _get_info(self, channel_id):
    headers = {
        'Authorization': f'Bot {self.token}'
    }

    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}', headers=headers)
    user_data = response.json()
    return user_data
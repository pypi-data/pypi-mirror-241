from ..abc import Channel, Guild, User

class ObjectSearch:
  def __init__(self, token):
    self.token = token

  def search_channel(self, channel_id: int):
    return Channel(channel_id, self.token)

  def search_guild(self, guild_id: int):
    return Guild(guild_id, self.token)

  def search_user(self, user_id: int):
    return User(user_id, self.token)

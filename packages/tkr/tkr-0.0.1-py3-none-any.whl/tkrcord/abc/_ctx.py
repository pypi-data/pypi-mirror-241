import aiohttp
from ._user import User
from ._bot import Bot
from ._guild import Guild
from ._message import Message

class Context:
  class ctx:
    def __init__(self, token):
      self.token = token

    async def send(self, content=None, embed=None, components=None, channel_id=None, reply_message_id=None):
        if channel_id is None:
            channel_id = self.channel_id

        async with aiohttp.ClientSession() as session:
            headers = {
                'Authorization': f'Bot {self.token}',
                'Content-Type': 'application/json'
            }
            payload = {
                'content': content,
                'embed': embed,
                'components': components,
                'message_reference': {
                    'message_id': reply_message_id
                } if reply_message_id else None
            }
            url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
            await session.post(url, headers=headers, json=payload)


    async def reply(self, content=None, embed=None, components=None, message_id=None):
      if message_id is None: message_id = self.message_id
      await self.send(content, embed, components, reply_message_id=message_id)

    async def delete(self, message_id=None):
      if message_id is None: message_id = self.message_id
      async with aiohttp.ClientSession() as session:
          headers = {
              'Authorization': f'Bot {client.Token}'
          }
          url = f'https://discord.com/api/v9/channels/{self.channel_id}/messages/{message_id}'
          await session.delete(url, headers=headers)

    async def edit(self, content=None, embed=None, components=None):
      message_id = self.message_id
      async with aiohttp.ClientSession() as session:
          headers = {
              'Authorization': f'Bot {self.token}',
              'Content-Type': 'application/json'
          }
          payload = {
              'content': content,
              'embed': embed,
              'components': components
          }
          url = f'https://discord.com/api/v9/channels/{self.channel_id}/messages/{message_id}'
          await session.patch(url, headers=headers, json=payload)

  class MsgCtx(ctx):
    def __init__(self, context, token):
        super().__init__(token = token)
        self.message = Message(context, token)
        self.message_id = self.message.id
        self.channel_id = self.message.channel.id
        self.author = self.message.author
        self.guild = self.message.guild
        self.channel = self.message.channel

  class InitCtx(ctx):
    def __init__(self, context, token):
      super().__init__(token = token)
      self.application = Bot(token)
      self.version = context.get('v')
      self.user_settings = context.get('user_settings')
      self.user = self.application
      self.session_type = context.get('session_type')
      self.session_id = context.get('session_id')
      self.resume_gateway_url = context.get('resume_gateway_url')
      self.relationships = context.get('relationships')
      self.private_channels = context.get('private_channels')
      self.presences = context.get('presences')
      self.guilds = context.get('guilds')
      self.guild_join_requests = context.get('guild_join_requests')
      self.geo_ordered_rtc_regions = context.get('geo_ordered_rtc_regions')
      self.auth = context.get('auth')
      self._trace = context.get('_trace')
      self.session_lookup_time = context.get('session_lookup_time')
      self.session_lookup_finished = context.get('session_lookup_finished')
      self.discord_sessions_prd_2 = context.get('discord-sessions-prd-2-201')
      self.starting_guild_connect = context.get('starting_guild_connect')
      self.guilds_started = context.get('guilds_started')
      self.guilds_connect = context.get('guilds_connect')
      self.presence_started = context.get('presence_started')
      self.build_ready = context.get('build_ready')
      self.clean_ready = context.get('clean_ready')
      self.optimize_ready = context.get('optimize_ready')
      self.split_ready = context.get('split_ready')


  class MemberCtx(ctx):
    def __init__(self, context, token):
      super().__init__(token = token)
      self.author = User(context.get('user').get('id'), token)

  class GuildCtx(ctx):
    def __init__(self, context, token):
      super().__init__(token = token)
      self.guild = Guild(context.get('id'), token)

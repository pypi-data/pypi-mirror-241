import aiohttp
import asyncio

from ..abc import Context, Embed

class WSEvent:
    def __init__(self, message, client):
        self.ws = client.ws
        self.wsclient = client
        self.client = client.client
        if message.type == aiohttp.WSMsgType.TEXT:
          self.data = message.json()


        self._on_ready = None
        self._on_message = None

    async def heartbeat(self, heartbeat_interval):
        while True:
            await asyncio.sleep(heartbeat_interval)
            await self.ws.send_json({'op': 1, 'd': None})

    async def process_op(self):
      if self.data['op'] == 10:
        heartbeat_interval = self.data['d']['heartbeat_interval'] / 1000.0
        asyncio.ensure_future(self.heartbeat(heartbeat_interval))

      elif self.data['op'] == 0:  
        event_type = self.data['t']
        event_data = self.data['d']

        await self.event_handle(event_type, event_data)

    async def event_handle(self, event_type, event_data):
      if event_type == 'READY':
        ctx = Context.InitCtx(event_data, self.client.token)
        self.wsclient.session_id = ctx.session_id
        self.client.session_id = ctx.session_id
        if 'on_ready' in self.client.events: await self.client.events['on_ready'](ctx)


      elif event_type == 'MESSAGE_CREATE':
          content = event_data.get('content')
          content_split = content.split(' ', 1)
          event_content = content_split[0]
          content_vars = []

          if len(content_split) > 1:
            content_vars = content_split[1].split(', ')

          ctx = Context.MsgCtx(event_data, self.client.token)
          if 'on_message' in self.client.events: await self.client.events['on_message'](ctx, ctx.message.content)

          if event_content in list(self.client.commands.keys()):

            try:
              await self.client.commands[event_content](ctx, *content_vars)
            except Exception as e: f'error when running {event_data.get("content")} <|> {e}'

          if event_content in list(self.client.aliases.keys()):

            try:
              await self.client.aliases[event_content](ctx, *content_vars)
            except Exception as e: f'error when running {event_data.get("content")} <|> {e}'

      elif event_type == 'MESSAGE_UPDATE':
        ctx = Context.MsgCtx(event_data, self.client.token)
        if 'on_message_update' in self.client.events: await self.client.events['on_message_update'](ctx)

      elif event_type == 'MESSAGE_DELETE':
        ctx = Context.MsgCtx(event_data, self.client.token)
        if 'on_message_delete' in self.client.events: await self.client.events['on_message_delete'](ctx)

      elif event_type == 'GUILD_CREATE':
        ctx = Context.GuildCtx(event_data, self.client.token)
        if 'on_guild_join' in self.client.events: await self.client.events['on_guild_join'](ctx)

      elif event_type == 'GUILD_UPDATE':
        ctx = Context.GuildCtx(event_data, self.client.token)
        if 'on_guild_update' in self.client.events: await self.client.events['on_guild_update'](ctx)

      elif event_type == 'GUILD_DELETE':
        ctx = Context.GuildCtx(event_data, self.client.token)
        if 'on_guild_leave' in self.client.events: await self.client.events['on_guild_leave'](ctx)
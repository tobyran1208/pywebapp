import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

async def index(request):
    return web.Response(body=b'<h1>Awesom</h1>', content_type='text/html')

async def init_app():
    app = web.Application()
    app.add_routes([web.get('/',index)])
    return app

loop = asyncio.get_event_loop()
app = loop.run_until_complete(init_app())
web.run_app(app, port='9088', host='127.0.0.1')
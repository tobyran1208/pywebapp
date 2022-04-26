import asyncio
import orm
from models import User

async def test():
    await orm.create_pool(loop=loop, user='root', password='password', db='awesome')

    u = User(name='Admin', email='admin@admin.com', password='123456', admin=True, image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
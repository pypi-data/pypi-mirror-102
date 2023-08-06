from asgi_lifespan import LifespanManager
from httpx import AsyncClient


async def testclient(app):
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://testserver") as client:
            yield client

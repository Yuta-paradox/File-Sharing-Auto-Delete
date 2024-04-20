# (©) Itz_Zeno
# Movie Channel @Netflix_Dual
# Anime Channel @Anime_Wide




from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app


# (©) Itz_Zeno
# Movie Channel @Netflix_Dual
# Anime Channel @Anime_Wide

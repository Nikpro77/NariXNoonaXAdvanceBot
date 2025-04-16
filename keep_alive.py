from aiohttp import web

async def handle(request):
    return web.Response(text="Bot is running")

app = web.Application()
app.router.add_get("/", handle)

def keep_alive():
    web.run_app(app, port=8030)
  

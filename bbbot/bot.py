import discord
from bbbot.config import get_cfg
from bbbot.bestbuy import availability
import asyncio

FORMAT_STR = "👀👀👀👀 PRODUCT CAME IN STOCK GO %s GO NOW GET THE JUICE 👀👀👀👀👀👀"

client = discord.Client()
discord_cfg = get_cfg("discord")
bestbuy_cfg = get_cfg('bestbuy')

@client.event
async def on_ready():
    global user
    user = await client.fetch_user(discord_cfg['user_id'])
    await check_bestbuy_loop()
    print('We have logged in as {0.user}'.format(client))

async def check_bestbuy_loop():
    while True:
        await check_bestbuy()
        await asyncio.sleep(5)


async def check_bestbuy():
    if availability(bestbuy_cfg["product"]):
        await user.send(FORMAT_STR % bestbuy_cfg["product"])
    # This works ^

client.run(discord_cfg['token'])
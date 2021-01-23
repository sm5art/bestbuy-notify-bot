import discord

client = discord.Client()

my_id = "asdf"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user = client.get_user(my_id)
    await user.send('👀')
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    # This works ^

client.run('token')
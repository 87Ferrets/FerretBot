import discord

TOKEN = 'NzE0MTc5NTE0NDM1MTA4ODY0.Xsq5xw.x3No9lL3d-oQc4a7Lkdutb49nSA'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('~acegg'):
        await message.delete()
        await message.channel.send("Ferret Master Official is a person who likes animal crossing but doesn't have a switch and therefore can't play his wanted game, New Horizons.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
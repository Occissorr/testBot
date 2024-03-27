import discord

TOKEN = 'MTIyMjU4MTI1NzkwOTgyOTc0Mw.GiexV7.VEGEcTjt2KD6MOnRNW7XD3DZo2al3jQoLUXevs'

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)

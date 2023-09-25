import discord
from discord.ext import commands
from config import CHANNEL, TOKEN
import nike

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online)
    print("Succesfully logged in!")

@bot.event
async def on_message(message):
    message_content = message.content.lower()
    if message.channel.name == CHANNEL:
        if message_content.startswith('$nike'):
            SKU = message_content.split(' ')[1]
            print(SKU)
            nk = nike.nike(SKU)
            valNike = ''
            for x in nk:
                valNike+=f'{x} | {nk[x]}\n'
            embed = discord.Embed(title='asdasdasd', description='asdsada')
            embed.add_field(name=f'{SKU}',value=valNike, inline=True)
            await message.channel.send(embed = embed)
            print('Message Sent!')

bot.run(TOKEN)
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(intents=intents,command_prefix='!!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

async def my_command(ctx):
    await ctx.send("You ran my_command.")

TOKEN = 'YOURTOKEN'
bot.run(TOKEN)

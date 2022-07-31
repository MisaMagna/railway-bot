import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Bot Ready!")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def pong(ctx):
    await ctx.send("ping")

@bot.command()
async def lechuga(ctx):
    await ctx.send("Es un perturbado")


if __name__ == "__main__":
    bot.run(TOKEN)

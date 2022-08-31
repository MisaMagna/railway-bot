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
async def samurai(ctx):
    await ctx.send("Doges together, samurai forever!")


@bot.command()
async def attack(ctx):
    await ctx.send("Doge's art: Bonk!")


@bot.command()
async def nya(ctx):
    await ctx.send("Silence wench!")
    await ctx.send("I don't want to be horny anymore")
    await ctx.send("I just want to be happy~")


if __name__ == "__main__":
    bot.run(TOKEN)

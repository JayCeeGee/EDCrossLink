import discord
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

fp_info = open("token.txt", "r")
token = fp_info.read()
fp_info.close()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('!ragequit'):
        msg = '{0.author.mention} has rage quit - Goodbye!! http://giphy.com/gifs/triggered-kRgj0fQLxhVoA'.format(message)
    await bot.send_message(message.channel, msg)


@bot.command()
async def joined(member: discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


bot.run(token)

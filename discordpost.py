import discord
from discord.ext import commands
import logging
from time import gmtime, strftime
import requests
import json
import random
import feedparser
import os
import subprocess
import urllib
import pygsheets


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
client = commands.Bot(command_prefix='!', description=description)


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

fp_info = open("token.txt", "r")
token = fp_info.read()
fp_info.close()


def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Primate Discipline'))


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif message.content.startswith('!help'):
        print('woop')
        msg = await client.send_message(message.channel, 'Available commands: fort, prep, expand, galnet, chuck, time')
        client.send_message(msg)

    elif message.content.startswith('!ragequit'):
        msg = await client.send_message(message.channel, '{0.author.mention} has rage quit - Goodbye!! http://giphy.com/gifs/triggered-kRgj0fQLxhVoA'.format(message))
        client.send_message(message.channel, msg)

    elif message.content.startswith('!facepalm'):
        msg = await client.send_message(message.channel, 'http://imgur.com/a/HAGd7')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!escalate'):
        msg = await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/204927799423664137/301083037138157568/15m34n.png')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!dave'):
        msg = await client.send_message(message.channel, 'https://cdn.meme.am/cache/instances/folder165/500x/71341165.jpg')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!thumb'):
        user = discord.User(id=108520493966979072)
        msg = await client.send_message(message.channel, '{0.mention} We need you Thumbelina - https://s-media-cache-ak0.pinimg.com/originals/f0/99/fd/f099fdfe64b9a2545f26b8d3c9071eb3.jpg'.format(user))
        client.send_message(message.channel, msg)

    elif message.content.startswith('!salt'):
        msg = await client.send_message(message.channel, 'https://i.imgflip.com/15ckrs.jpg')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!announce'):
        line = message.content
        word, space, rest = line.partition(' ')
        tannoycontent = rest
        print(tannoycontent)
        msg = await client.send_message(discord.Object(id='144116783056420875'), tannoycontent)
        client.send_message(msg)

    elif message.content.startswith('!shout'):
        line = message.content
        word, space, rest = line.partition(' ')
        tannoycontent = rest
        msg = await client.send_message(discord.Object(id='121698824682078208'), tannoycontent)
        client.send_message(msg)

    elif message.content.startswith('!explore'):
        msg = await client.send_message(message.channel, 'Exploration is not a valid play style, your argument is invalid.')
        client.send_message(msg)

    elif message.content.startswith('!kalak'):
        msg = await client.send_message(message.channel, 'I may be wrong, but I believe Kalak needs another 10k forts. Thank you please!')
        client.send_message(msg)

    elif message.content.startswith('!chuck'):
        link = "http://api.icndb.com/jokes/random"
        f = requests.get(link)

        j = json.loads(f.text)
        value = (j['value'])
        print(value['joke'])
        msg = await client.send_message(message.channel, value['joke'])
        client.send_message(msg)

    elif message.content.startswith('!time'):
        gametime = strftime("%m-%d %H:%M:%S", gmtime())
        msg = await client.send_message(message.channel, 'The current time is 3303-{}'.format(gametime))
        client.send_message(msg)

    elif message.content.startswith('!galnet'):
        feed = feedparser.parse('http://proxy.gonegeeky.com/edproxy/')
        msg = await client.send_message(message.channel, 'Latest Galnet Story:   {}'.format(feed['entries'][0].title))
        msg2 = await client.send_message(message.channel, 'Link:   {}'.format(feed['entries'][0].link))
        client.send_message(msg)
        client.send_message(msg2)

    elif message.content.startswith('!fort'):

        gc = pygsheets.authorize(outh_file='client_secret.json', outh_nonlocal=True)
        sh = gc.open('System Calulator')
        wks = sh.sheet1
        fort1 = wks.get_value('A5')
        fort2 = wks.get_value('A6')
        fort3 = wks.get_value('A7')
        fort4 = wks.get_value('A8')
        fort5 = wks.get_value('C5')
        fort6 = wks.get_value('C6')
        fort7 = wks.get_value('C7')

        msg = await client.send_message(discord.Object(id='181004780489932800'), '{0.author.mention}, the current fort targets are:'.format(message))
        msg2 = await client.send_message(discord.Object(id='181004780489932800'), "For Large Pads: {}, {}, {}, {}".format(fort1, fort2, fort3, fort4))
        msg3 = await client.send_message(discord.Object(id='181004780489932800'), "For Small/Medium Pads: {}, {}, {}".format(fort5, fort6, fort7))
        client.send_message(msg)
        client.send_message(msg2)
        client.send_message(msg3)

    elif message.content.startswith('!prep'):

        gc = pygsheets.authorize(outh_file='client_secret.json', outh_nonlocal=True)
        sh = gc.open('System Calulator')
        wks = sh.sheet1

        prep = wks.get_value('A13')

        msg = await client.send_message(discord.Object(id='181004780489932800'), '{0.author.mention}, the current prep target is:'.format(message))
        msg2 = await client.send_message(discord.Object(id='181004780489932800'), '{}'.format(prep))
        client.send_message(msg)
        client.send_message(msg2)

    elif message.content.startswith('!expand'):
        msg = await client.send_message(message.channel, "{0.author.mention}, are you mental, it's not like we have enough to do".format(message))
        client.send_message(msg)

    elif message.content.startswith('!civilwar'):

        fp_cwar = open("cw.txt", "r")
        cwarinfo = fp_cwar.read().split('^')
        fp_cwar.close()

        msg = await client.send_message(discord.Object(id='138036649694068736'), '{0.author.mention}, the current civil wars are:'.format(message))
        client.send_message(msg)
        for cw in cwarinfo:
            msg = await client.send_message(discord.Object(id='138036649694068736'), '{}'.format(cw))
            client.send_message(msg)

    elif message.content.startswith('!ships'):
        line = message.content
        word, space, rest = line.partition(' ')
        cmd_var = rest
        command = '/usr/bin/python3.6 /home/shared/trade/tradedangerous/trade.py shipvendor {}'.format(
            cmd_var)
        for line in run_command(command):
            line = line.decode('UTF-8')
            msg = await client.send_message(message.channel, line)
            client.send_message(msg)

    elif message.content.startswith('!rares'):
        line = message.content
        word, space, rest = line.partition(' ')
        cmd_var = rest
        command = '/usr/bin/python3.6 /home/shared/trade/tradedangerous/trade.py rares {} --ly 50'.format(
            cmd_var)
        for line in run_command(command):
            line = line.decode('UTF-8')
            msg =await client.send_message(message.channel, line)
            client.send_message(msg)


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))


client.run(token)

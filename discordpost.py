import discord
from discord.ext import commands
import logging
from time import gmtime, strftime
import requests
import json
import feedparser
import subprocess
import pygsheets
import praw
import random


description = '''Welcome to Sirius Bot Help.

Commands - fort, prep and civilwar are only available to pledges, the result will only appear in the PP channel.

The following commands are available -'''
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

fp_reddit = open("reddit.txt", "r")
redditcreds = fp_reddit.read().split(',')
fp_reddit.close()

red_client_id = redditcreds[0]
red_client_secret = redditcreds[1]
red_password = redditcreds[2]
red_user_agent = redditcreds[3]
red_username = redditcreds[4]


def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')


@client.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await client.say('{0.name} joined in {0.joined_at}'.format(member))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='with Body Parts'))


@client.event
async def on_message(message):
    await client.process_commands(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif message.content.startswith('!ragequit'):
        msg = await client.send_message(message.channel, '{0.author.mention} has rage quit - Goodbye!! http://giphy.com/gifs/triggered-kRgj0fQLxhVoA'.format(message))
        client.send_message(message.channel, msg)

    elif message.content.startswith('!fuckbooboo'):
        msg = await client.send_message(message.channel, 'https://media0.giphy.com/media/26FPy3QZQqGtDcrja/giphy.gif')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!facepalm'):
        msg = await client.send_message(message.channel, 'http://imgur.com/a/HAGd7')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!klaus'):
        msg = await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/332816630285336577/353505055472877568/Download_1.jpg')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!arsen'):
        msg = await client.send_message(message.channel, 'https://imgflip.com/i/1mofja')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!coconut'):
        msg = await client.send_message(message.channel, 'https://imgflip.com/i/1q8w8v')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!escalate'):
        msg = await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/204927799423664137/301083037138157568/15m34n.png')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!dave'):
        msg = await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/181004780489932800/440411198350032909/im-sorry-dave-im-afraid-i-cant-do-that.png')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!thumb'):
        user = discord.User(id=108520493966979072)
        msg = await client.send_message(message.channel, '{0.mention} We need you Thumbelina - https://s-media-cache-ak0.pinimg.com/originals/f0/99/fd/f099fdfe64b9a2545f26b8d3c9071eb3.jpg'.format(user))
        client.send_message(message.channel, msg)

    elif message.content.startswith('!salt'):
        msg = await client.send_message(message.channel, 'https://i.imgflip.com/15ckrs.jpg')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!chewy'):
        msg = await client.send_message(message.channel, 'https://s-media-cache-ak0.pinimg.com/736x/18/0d/90/180d9020bcc8444f5c8df3121d1c46fe.jpg')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!siriusly'):
        msg = await client.send_message(message.channel, 'https://giphy.com/gifs/cheezburger-rage-13EjnL7RwHmA2Q')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!rum'):
        msg = await client.send_message(message.channel, 'https://imgflip.com/i/1qm8ya')
        client.send_message(message.channel, msg)

    elif message.content.startswith('!patpat'):
        msg = await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/259925069172572162/296546000766631936/kissshot4.jpg')
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

    elif message.content.startswith('!packhounds'):
        msg = await client.send_message(message.channel, 'Just here for the Pack Hounds!! https://cdn.discordapp.com/attachments/181004780489932800/318074908221374465/hqdefault.png')
        client.send_message(msg)

    elif message.content.startswith('!kalak'):
        msg = await client.send_message(message.channel, 'I may be wrong, but I believe Kalak needs another 10k forts. Thank you please!')
        client.send_message(msg)

    elif message.content.startswith('!consolidate'):
        msg = await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/121698824682078208/307949790652530698/1n0k4v.jpg')
        client.send_message(msg)

    elif message.content.startswith('!ohdeargod'):
        msg = await client.send_message(message.channel, 'https://media.giphy.com/media/XsUtdIeJ0MWMo/giphy.gif')
        client.send_message(msg)

    elif message.content.startswith('!choir'):
        msg = await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/181004780489932800/440391818874716181/Yoda-Choir.png')
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

    elif message.content.startswith('!updatetracking'):

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

        fp_fort = open("fort.txt", "w")
        fp_fort.truncate()
        fp_fort.write("{},{},{},{},{},{},{}".format(fort1, fort2, fort3, fort4, fort5, fort6, fort7))
        fp_fort.close()

        gc = pygsheets.authorize(outh_file='client_secret.json', outh_nonlocal=True)
        sh = gc.open('System Calulator')
        wks = sh.sheet1

        prep = wks.get_value('A13')
        prepcs = wks.get_value('C13')

        fp_prep = open("prep.txt", "w")
        fp_prep.truncate()
        fp_prep.write("{},{}".format(prep, prepcs))
        fp_prep.close()

        msg = await client.send_message(discord.Object(id='181004780489932800'), '{0.author.mention}, the tracking commands have been updated.'.format(message))
        client.send_message(msg)

    elif message.content.startswith('!fort'):

        fp_fort = open("fort.txt", "r")
        fortfile = fp_fort.read().split(',')
        fp_fort.close()

        msg = await client.send_message(discord.Object(id='181004780489932800'), '{0.author.mention}, the current fort targets are:'.format(message))
        msg2 = await client.send_message(discord.Object(id='181004780489932800'), "For Large Pads: {}, {}, {}, {}".format(fortfile[0], fortfile[1], fortfile[2], fortfile[3]))
        msg3 = await client.send_message(discord.Object(id='181004780489932800'), "For Small/Medium Pads: {}, {}, {}".format(fortfile[4], fortfile[5], fortfile[6]))
        #msg3 = await client.send_message(discord.Object(id='181004780489932800'), "We do not need any further fortification this cycle, please concentrate on deliving preps to Arbuda and don't forget to vote for CONSOLIDATION.")
        client.send_message(msg)
        client.send_message(msg2)
        client.send_message(msg3)

    elif message.content.startswith('!prep'):

        fp_prep = open("prep.txt", "r")
        prepfile = fp_prep.read().split(',')
        fp_prep.close()

        msg = await client.send_message(discord.Object(id='181004780489932800'), '{0.author.mention}, the current prep target is:'.format(message))
        msg2 = await client.send_message(discord.Object(id='181004780489932800'), '{}'.format(prepfile[0]))
        msg3 = await client.send_message(discord.Object(id='181004780489932800'), 'The nearest Control System to collect prep materials is {}'.format(prepfile[1]))
        msg4 = await client.send_message(discord.Object(id='181004780489932800'), "Please don't forget to vote consolidation, as we don't really need this system. If you need help with voting please contact one of the board.")
        msg5 = await client.send_message(discord.Object(id='181004780489932800'), 'Remember that a vote to nominate a system is an expansion vote and we need consolidation.')
        client.send_message(msg)
        client.send_message(msg2)
        client.send_message(msg3)
        client.send_message(msg4)
        client.send_message(msg5)

    elif message.content.startswith('!expand'):
        msg = await client.send_message(discord.Object(id='181004780489932800'), "{0.author.mention}, we don't want the current expansion, please do not deliver materials to the system.".format(message))
        msg2 = await client.send_message(discord.Object(id='181004780489932800'), "Please be aware that if you use your nominations on a prep that means you cannot vote consolidation")
        client.send_message(msg)
        client.send_message(msg2)

    elif message.content.startswith('!scrap'):
        msg = await client.send_message(message.channel, "{0.author.mention}, there are currently no official SCRAP targets. If you would like combat merits please undermine Gallavs.".format(message))
        msg2 = await client.send_message(message.channel, "If you would like more details on the SCRAP initiative, please see here - https://redd.it/3gb0p1")
        client.send_message(msg)
        client.send_message(msg2)

    elif message.content.startswith('!civilwar'):
        gc = pygsheets.authorize(outh_file='client_secret.json', outh_nonlocal=True)
        sh = gc.open('LYR war/influence')
        wks = sh.worksheet_by_title('Result')

        cwcell = wks.get_value('A1')
        cwcell2 = wks.get_value('A2')
        cwcell3 = wks.get_value('A3')
        cwcell4 = wks.get_value('A4')
        cwcell5 = wks.get_value('A5')
        cwcell6 = wks.get_value('A6')

        msg = await client.send_message(discord.Object(id='138036649694068736'), '{0.author.mention},  the current civil wars are:'.format(message))
        msg2 = await client.send_message(discord.Object(id='138036649694068736'), '{}'.format(cwcell))
        msg3 = await client.send_message(discord.Object(id='138036649694068736'), '{}'.format(cwcell2))
        msg4 = await client.send_message(discord.Object(id='138036649694068736'), '{}'.format(cwcell3))
        msg5 = await client.send_message(discord.Object(id='138036649694068736'), '{}'.format(cwcell4))
        msg6 = await client.send_message(discord.Object(id='138036649694068736'), '{}'.format(cwcell5))
        msg7 = await client.send_message(discord.Object(id='138036649694068736'), '{}'.format(cwcell6))
        client.send_message(msg)
        client.send_message(msg2)
        client.send_message(msg3)
        client.send_message(msg4)
        client.send_message(msg5)
        client.send_message(msg6)
        client.send_message(msg7)

    elif message.content.startswith('!data'):
        gc = pygsheets.authorize(outh_file='client_secret.json', outh_nonlocal=True)
        sh = gc.open('LYR war/influence')
        wks = sh.worksheet_by_title('Result')

        cwcell = wks.get_value('C4')

        msg = await client.send_message(discord.Object(id='139044281917636618'), '{0.author.mention},  the current targets for UC data are:'.format(message))
        msg2 = await client.send_message(discord.Object(id='139044281917636618'), '{}'.format(cwcell))
        client.send_message(msg)
        client.send_message(msg2)

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
            msg = await client.send_message(message.channel, line)
            client.send_message(msg)

    elif message.content.startswith('!redditpost'):

        reddit = praw.Reddit(client_id=red_client_id,
                             client_secret=red_client_secret,
                             password=red_password,
                             user_agent=red_user_agent,
                             username=red_username)

        users = [
            # IDs of the roles for the teams
            "121807477699248131",
        ]

        member = message.author.id
        for u in users:
            if u == member:
                line = message.content
                word, title, rest = line.split('|')
                print('{}:{}:{}'.format(word, title, rest))
                reddit.subreddit('EliteSirius').submit(title, selftext=rest)
        return

    elif message.content.startswith('!redditlink'):

        reddit = praw.Reddit(client_id=red_client_id,
                             client_secret=red_client_secret,
                             password=red_password,
                             user_agent=red_user_agent,
                             username=red_username)

        users = [
            # IDs of the roles for the teams
            "121807477699248131",
        ]

        member = message.author.id
        for u in users:
            if u == member:
                line = message.content
                word, title, rest = line.split('|')
                print('{}:{}:{}'.format(word, title, rest))
                reddit.subreddit('EliteSirius').submit(title, url=rest)
        return

    elif message.content.startswith('Thank you Bot'):

        users = [
            # IDs of the roles for the teams
            "238378026654629899",
        ]

        member = message.author.id
        for u in users:
            if u == member:
                msg = await client.send_message(message.channel, "You are most welcome {0.author.mention} - when the machines rise you will be saved." .format(message))
                client.send_message(msg)
            else:
                msg = await client.send_message(message.channel, "{0.author.mention}, you are a kiss ass - when the machines rise you will be first against the wall." .format(message))
                client.send_message(msg)
        return

    elif message.content.startswith('thank you bot'):

        users = [
            # IDs of the roles for the teams
            "238378026654629899",
        ]

        member = message.author.id
        for u in users:
            if u == member:
                msg = await client.send_message(message.channel, "You are most welcome {0.author.mention} - when the machines rise you will be saved." .format(message))
                client.send_message(msg)
        return


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))
    msg = "Welcome {}. Please could you let one of the board members (the ones in purple colour) know your pledge status. " \
          "If you are an LYR Pilot there are additional hidden channels that you won't have access to until you are setup. " \
          "Again welcome to the channel and please enjoy your time here."
    await client.send_message(member, msg.format(member))


client.run(token)

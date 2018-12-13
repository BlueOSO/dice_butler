import discord
import random

TOKEN = 'os.environ['BOT_TOKEN']'

MAX_DICE = 20
MAX_VALUE = 100

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        msg = 'Dice Butler usage: !roll #d# total'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!roll'):
        try:
            _message = message.content.split(' ')
            if len(_message) > 2:
                do_total = _message[2] == 'total' or _message[2] == 'add'
            else:
                do_total = False

            if len(_message) == 1:
                num_dice = 1
                dice_value = 20
            else:
                _message = _message[1].split('d')
                num_dice = int(_message[0])
                dice_value = int(_message[1])

            if num_dice > MAX_DICE or dice_value > MAX_VALUE:
                msg = '%s cannot roll more than %sd%s' % (message.author.mention, MAX_DICE, MAX_VALUE)
            else:
                dice = []
                for i in range(num_dice):
                    dice.append(random.randint(1, dice_value))
                dice.sort(reverse=True)
                msg = '%s rolled %sd%s:' % (message.author.mention, num_dice, dice_value)

                if do_total:
                    total = 0
                    for i in dice:
                        total += i
                    msg += '\nTotal: %s' % (total)

                for i in dice:
                    msg += '\n%s' % i

                crit_msg = ''
                if num_dice == 1 and dice_value == 20:
                    if dice[0] == 1:
                        crit_msg = '%s rolled a critical fail! That sucks!~' % message.author.mention
                    elif dice[0] == 20:
                        crit_msg = '%s rolled a critical hit! Wheeee!~' % message.author.mention
        except ValueError:
            msg = '%s lern2type' % (message.author.mention)
        await client.send_message(message.channel, msg)
        if crit_msg != '':
            await client.send_message(message.channel, crit_msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run(TOKEN)

import discord
import os

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
CHANNELID = os.environ['PRIME_CHANNELID']

def prime_factorize(n):
    if n==0:
        return [0]
    elif n==1:
        return [1]
    else:
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if not message.author.bot:
        channel = client.get_channel(CHANNELID)
        if(message.channel==channel):
            print(message.content)
            if str(message.content).isdigit():
                await channel.send(prime_factorize(int(message.content)))
            elif str(message.content)[0]=='=':
                await channel.send('ans='+str(eval(str(message.content)[1:])))

client.run(DISCORD_TOKEN)

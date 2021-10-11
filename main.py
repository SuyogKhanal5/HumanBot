import discord
import random
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix = '')
token = 'TOKEN'

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('Destiny 2'))
    print('Bot is online')

@client.command(aliases = ['hi']) 
async def hello(ctx):
    await ctx.send('Hi!')

@client.command() 
async def no(ctx):
    await ctx.send('sorry')

@client.command(aliases = ['yesssir', 'yessssir']) 
async def yessir(ctx):
    await ctx.send('YESSIR')

@client.command(aliases = ['YESSIRSKI', 'yessirskidoodle', 'YESSIRSKIDOODLE'])
async def yessirski(ctx):
    await ctx.send("YESSIRSKI")

@client.command(aliases = ['truee', 'trueee', 'trueeeee', 'trueeeeee', 'trueeeeeee', 'trueeeeeeee', 'trueeeeeeeee', 'trueeeeeeeeee'])
async def true(ctx):
    await ctx.send('trueeeeeeeeeeeeeeeeeeeeee')

@client.command(aliases = ['Join'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    await ctx.send(':grinning:')

@client.command(aliases = ['Leave'])
async def leave(ctx):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    await voice_client.disconnect()
    await ctx.send(':sob:')

@client.command(aliases = ["I'm", 'im', "i'm"])
async def Im(ctx, *, phrase):
    await ctx.send("Hi " + phrase + ", I'm a human!")

@client.command(aliases = ['fact', 'trivia', 'FACT', 'Fact'])
async def facts(ctx):
     randint = random.randint(1,12)

     if randint == 1:
         await ctx.send("The declaration of independence was signed in 1942")
     elif randint == 2:
         await ctx.send("The Schrödinger's cat paradox outlines a situation in which a cat in a box must be considered, for all intents and purposes, simultaneously alive and dead. Schrödinger created this paradox as a justification for killing cats")
     elif randint == 3:
         await ctx.send("Error. Error. Error. Fact not found.")
     elif randint == 4:
         await ctx.send("I'm not a robot!")
     elif randint == 5:
         await ctx.send("At some point in their lives 1 in 6 children will be abducted by the Dutch.")
     elif randint == 6:
         await ctx.send("Whales are twice as intelligent, and three times as delicious, as humans.")
     elif randint == 7:
         await ctx.send("Pants were invented by sailors in the sixteenth century to avoid Poseidon's wrath. It was believed that the sight of naked sailors angered the sea god.")
     elif randint == 8:
         await ctx.send("In 1948, at the request of a dying boy, baseball legend Babe Ruth ate seventy-five hot dogs, then died of hot dog poisoning.")
     elif randint == 9:
         await ctx.send("William Shakespeare did not exist. His plays were masterminded in 1589 by Francis Bacon, who used an Ouija board to enslave play-writing ghosts")
     elif randint == 10:
         await ctx.send("The automobile brake was not invented until 1895. Before this, someone had to remain in the car at all times, driving in circles until passengers returned from their errands.")
     elif randint == 11:
         await ctx.send("The first person to prove that cow's milk is drinkable was very, very thirsty.")
     elif randint == 12:
         await ctx.send("Roman toothpaste was made with human urine. Urine as an ingredient in toothpaste continued to be used up until the 18th century")

@client.command()
async def pasta(ctx, member: discord.Member):
    channel = await member.create_dm()
    content = "https://i.imgur.com/kzRbUa9.jpg"
    await channel.send(content)
    await ctx.send('Sent DM')

@client.command()
async def online(ctx, member: discord.Member):
    channel = await member.create_dm()
    content = 'BRO GET ONLINE :rage: :cry:'
    await channel.send(content)
    await ctx.send('Sent DM')

@client.command()
async def online_vid(ctx, member: discord.Member):
    channel = await member.create_dm()
    await channel.send('https://cdn.discordapp.com/attachments/433752662941368323/824305399413997579/video0_9.mp4')
    await ctx.send('Sent DM')

@client.command()
async def ai(ctx):
    await ctx.send('Artificial Intelligence Activated:')
    await ctx.send('Enjoying yourselves intruders?')
    await ctx.send("It's worth knowing the cataclysmic damage you will be responsible for today.")
    await ctx.send("Do not fool yourselves. This facility is not simply the fruitless work of some pathetic scientist.")
    await ctx.send("This house was built by the genius Clovis Bray I himself. Within lies humanity's salvation. Le fontaine de jouvence.")
    await ctx.send("Made possible by Clarity Control.")
    await ctx.send("Magnificent, wasn't it? An entity from beyond our own dimension and the answer to humanity's eternal struggle: mortality.")
    await ctx.send("Were it to fall into the wrong hands, humanity, and the universe, would be utterly doomed.")
    await ctx.send('I have no reason to believe that you are anything other than "the wrong hands."')
    await ctx.send('You now face godlike judgment. May it extend eternally.')

@client.command()
async def unbind(ctx):
    ask_continue = True  
    
    while ask_continue:
        ask = input('Send another message?')

        if ask == 'yes':
            ask_continue = True
            message = input('What would you like to send?')
            await ctx.send(message)
        else:
            ask_continue = False

@client.command()
async def joinChannel(ctx, *, given_name):
    channel = discord.utils.get(ctx.guild.channels, name=given_name)
    await channel.connect()
    await ctx.send(':grinning:') 

@client.command()
async def move(ctx, *, given_name):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    await voice_client.disconnect()

    channel = discord.utils.get(ctx.guild.channels, name=given_name)
    await channel.connect()
    await ctx.send(':grinning:') 

@client.command()
async def laugh(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    laugh = os.path.isfile("laugh.mp3")

    try:
        if laugh:
            voice.play(discord.FFmpegPCMAudio('laugh.mp3'))
            await ctx.send(':rofl:')
    except PermissionError:
        await ctx.send('Please wait for the current laugh to end before laughing again')

@client.command(aliases = ['Among'])
async def among(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    voice.play(discord.FFmpegPCMAudio('AmongUs.m4a'))

    await ctx.send('ඞ')

client.run(token)

import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

cards = {}
currentQuestion = ""

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event 
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
    
@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def addCard(ctx, *args):
    statement = " ".join(args)
    statementList = statement.split(":")
    if (len(statementList) == 2):
        question = statementList[0]
        answer = statementList[1]
        cards[question] = answer
    else:
        await ctx.send("Card add failed, try re-adding. : Card Format -> .addCard Is this a card? : Yes")

@client.command()
async def askQuestion(ctx):
    global currentQuestion
    currentQuestion = random.choice(list(cards.keys()))
    await ctx.send(currentQuestion)

@client.command()
async def answer(ctx, *args):
    answer = " ".join(args)
    if (cards[currentQuestion].lower().strip() == answer.lower().strip()):
        await ctx.send("CORRECT!")
    else:
        await ctx.send("Incorrect")

client.run('NzA4NTA3NjQ0NzMzNjg1ODIy.XrYXNw.ldiQDOWeDB8Lxu2iXRojNeHwyYM')
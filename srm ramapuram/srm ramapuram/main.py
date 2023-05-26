#main.py

from discord.ext import commands
import discord
from discord import File
from search import browse
import uuid
import requests
import shutil
from txt_from_img import txt
import os
from exif_data import get_info
from gdrive import auth, search_file
from model import locatee
from exif_info import misc_info


intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="H ", intents = intents)


@client.event
async def on_ready():
    print("Ready")

@client.command(pass_context = True)
async def hey(ctx):
    await ctx.channel.send("Welcome!!")


@client.command()
async def search(ctx):
    try:
        url = ctx.message.attachments[0].url
    except IndexError:
        print("No fille attached")
        await ctx.channel.send("No file attached")
    else:
        if url[0:26] == "https://cdn.discordapp.com":
            r = requests.get(url, stream=True)
            imgName = str(uuid.uuid4()) + '.jpg'
            with open(imgName, 'wb') as out_file:
                print(f"File saved as {imgName}") 
                shutil.copyfileobj(r.raw, out_file)
            texts = txt(imgName)
            await ctx.channel.send(browse(texts))
            os.remove(imgName)

@client.command()
async def info(ctx, name):
    auth()
    filee = search_file(name)
    locatee((get_info(filee))[0], (get_info(filee))[1])
    await ctx.channel.send(file = File('location.html'))
    await ctx.channel.send(misc_info(filee))

            

client.run('enter token value')

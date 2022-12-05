# bot.py
import os

import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(e):
    if e.author == client.user:
        return
        
    if e.content.lower().startswith("ligma"):
        await e.channel.send("balls")
        
    #if e.author.id == 302646759169982464:
    #    await e.add_reaction("🐀")
    #   test for adding reactions to my messages... but with an already existing emoji
        
    if e.author.id == 846292904992571392:
        ethanol = await e.guild.fetch_emoji(1045167854108016680)
        await e.add_reaction(ethanol)
      #  print(e.content)
      #  used the print to get the ID for the custom emoji that ended up being the bot's reaction :)
    
	
client.run("TOKEN")

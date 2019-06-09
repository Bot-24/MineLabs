import discord
from discord.ext import commands
import asyncio
from itertools import cycle

client = commands.Bot(command_prefix = '+')
status = ['mit der Community', 'auf MineLabs', 'mit LennexDev <3', '+help']

async def change_status():
	await client.wait_until_ready()
	msgs = cycle(status)
	
	while not client.is_closed:
		current_status = next(msgs)
		await client.change_presence(game=discord.Game(name=current_status))
		await asyncio.sleep(10)
		
@client.event
async def on_ready():
    print('Eingeloggt als MineLabsBot')
    print(client.user.name)
    print(client.user.id)
    print('------------')
        
@client.command()
async def ip ():
   await client.say("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   await client.say("IP : **Comming Soon!**")
   await client.say("PORT : 19132")
   await client.say("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

@client.command() 
async def invite ():
  await client.say("**Comming Soon!**")
  await client.say("Zum Inviten Des Bots!")
	
@client.command()
async def ping ():
	await client.say("Pong! 0ms")
	
@client.command()
async def joke ():
	await client.say("Was macht ein Tier in der disco, discotieren ahahahaha :joy: .")
	
@client.command()
async def coder ():
	await client.say("Der Coder ist:")
	await client.say("LennexDev :wink:")

@client.command()
async def hotdog ():
	await client.say("hotdog")
	
@client.command()
async def yt ():
	await client.say("Kommt noch!")
	
@client.command()
async def botowner ():
	await client.say("Dieser Bot gehört LennexDev")
	
@client.command()
async def h ():
	await client.say("————————————")
	await client.say("Commands:")
	await client.say("botowner")
	
client.loop.create_task(change_status())
client.run('process.env.BOT_TOKEN')
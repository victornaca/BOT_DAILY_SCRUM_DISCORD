import discord
import asyncio
import pytz
from datetime import datetime
from discord.ext import tasks

client = discord.Client(intents=discord.Intents.default())

@tasks.loop(seconds=30)
async def anuncio():
        while True:
                now = datetime.now(pytz.timezone('Etc/GMT+3'))
                current_time = now.strftime("%H:%M")
                print(current_time)
                if current_time == "22:40":
                        canal = client.get_channel(873013859428995089)
                        await canal.send("@everyone Se liga na Daily de hoje \n1º O que eu fiz hoje? \n2º O que eu vou fazer no dia seguinte de trabalho? \n3º Problemas que eu possa ter")
                        await asyncio.sleep(60)
                return

@client.event
async def on_ready():
        anuncio.start()

client.run('MTA3NjU1MTU1NzYxODg2ODM0NQ.GznJYl.6aJH3mrOjO-C4GBAjYyW3Hd79o-FyfEM27WaGg')
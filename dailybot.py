import discord
import asyncio
import pytz
from datetime import datetime, date
from discord.ext import tasks
client = discord.Client(intents=discord.Intents.default())

@tasks.loop(seconds=30)
async def anuncio():
        while True:
                ds = date.today().weekday()
                print(ds)
                now = datetime.now(pytz.timezone('Etc/GMT+3'))
                current_time = now.strftime("%H:%M")
                if ds == 5 or ds == 6:
                        print("Final de Semana")
                        await asyncio.sleep(86400)
                        break
                else:
                        print(current_time)
                        if current_time == "22:40":
                                canal = client.get_channel(873013859428995089)
                                await canal.send("@everyone Se liga na Daily de hoje \n1º O que eu fiz hoje? \n2º O que eu vou fazer no dia seguinte de trabalho? \n3º Problemas que eu possa ter")
                                await asyncio.sleep(60)
                return

@client.event
async def on_ready():
        anuncio.start()

client.run('MTA3NjU1MTU1NzYxODg2ODM0NQ.GQ98V7.cemYIU1dJJLqe5BeBhKCiadZwIOT-ftE3tnrH8')
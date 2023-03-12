import discord
import asyncio
import pytz
from datetime import datetime, date
from discord.ext import tasks

client = discord.Client(intents=discord.Intents.default()) #Acesso ao servidor do discord

@tasks.loop(seconds=30) #Inicio da taskloop
async def anuncio():

        while True: #Abertura do loop de verificação de dia da semana e hora
                ds = date.today().weekday() #Capturar dia da semana de hoje
                print(ds)
                now = datetime.now(pytz.timezone('Etc/GMT+3')) #Capturar datahora de agora com fuzo horario
                current_time = now.strftime("%H:%M") #Separar apenas hora/minuto

                if ds == 6 or ds == 7: #Verificar se o dia da semana é sabado ou domingo
                        print("Final de Semana")
                        await asyncio.sleep(86400) #loop de 24h
                        break

                else: #Se não for fim de semana irá seguir
                        print(current_time)

                        if current_time == "22:40": #Verificar se a hora/minuto de agora é igual 22:40
                                canal = client.get_channel('numero do canal') #Canal do discord que deseja enviar a mensagem
                                await canal.send("@everyone Se liga na Daily de hoje \n1º O que eu fiz hoje? \n2º O que eu vou fazer no dia seguinte de trabalho? \n3º Problemas que eu possa ter")
                                await asyncio.sleep(60) #pausa de 1 minuto na verificação
                return #Retorna ao loop

@client.event
async def on_ready(): #inicialização da função
        anuncio.start()

client.run('id do servidor') #ID do seu servidor
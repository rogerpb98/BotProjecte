import discord
from discord.ext import commands, tasks

token = 'Njk5OTIyOTA4MTc2MzE4NTU5.Xqq8-g.C2Yvl3C6v1X19saiNDHyHJ6ZOOI'

client = commands.Bot(command_prefix='!')

#####EVENTS#####

#Event que mostra per consola quan el bot es connecta al servidor.
@client.event
async def on_connect():
    print("S'ha connectat al servidor")

#Event que mostra per consola quan el bot es desconnecta del servidor.
@client.event
async def on_disconnect():
    print("S'ha desconnectat al servidor")

#Event que mostra per consola i mitjançant un missatge pel servidor quan el bot estigui llest per rebre comandes/tasques.
@client.event
async def on_ready():
    print("El bot està llest per ser utilitzat.")

#Aquest event notifica quan un usuari entra a un servidor on estigui el bot.
@client.event
async def on_member_join(member):
    print("L'usuari ",member," acaba d'entrar al servidor.")

#Aquest event notifica quan un usuari surt d'un servidor on estigui el bot.
@client.event
async def on_member_remove(member):
    print("L'usuari ",member," acaba de sortir del servidor.")
################

#####COMANDES#####

##################

#####TASKS#####

###############

client.run(token)
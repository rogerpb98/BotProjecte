import discord
import random
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

#comanda de prova per veure com enviar missatges per un canal de texte a Discord.
@client.command()
async def patata(ctx):
    await ctx.send('patata')

#Galeta de la fortuna, utilitzant la llibrería "random" el bot escollirà una frase de l'array "frases" aleatoriament i la mostrarà per discord.
@client.command()
async def fortuna(ctx):
    frases=[
        'Tendrás un día de alegrías y buenos momentos, disfrútalos como nunca.',
        'Concéntrate en lo que quieres lograr y ganaras. No lo olvides.',
        'El cielo sera tu limite, pues grandes acontecimientos te sucederán.',
        'Te sentirás feliz como un niño y veras al mundo con sus ojos.',
        'Vivirás tu vejez con comodidades y riquezas materiales.'
    ]
    await ctx.send(random.choice(frases))

##################

#####TASKS#####

###############

client.run(token)
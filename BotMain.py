import discord
import random
import asyncio
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
    print(client.user.name)
    print(client.user.id)
    print("El bot està llest per ser utilitzat.")

#Aquest event notifica quan un usuari entra a un servidor on estigui el bot.
@client.event
async def on_member_join(member):
    print("L'usuari ",member," acaba d'entrar al servidor.")

#Aquest event notifica quan un usuari surt d'un servidor on estigui el bot.
@client.event
async def on_member_remove(member):
    print("L'usuari ",member," acaba de sortir del servidor.")

#Event/comanda que mostra una imatge dintre de la carpeta.
@client.event
async def on_message(message):
    #Event de prova per veure com es poden fer comandes amb els events.
    if message.content.startswith('!eventest'):
        canal = message.channel
        await canal.send('Funciona')
    #Event/comanda que mostra una imatge dintre de la carpeta.
    if message.content.startswith('!imatge'):
        #Buscar forma de interactuar amb el bot per decidir si la imatge será d'animals o d'insectes
        canal = message.channel
        misatge = await canal.send("Reacciona a aquest missatge amb un dels seguents emojis \n :cat: Fotografia d'un animal \n :bee: Fotografia d'un insecte")
        def check(reaction, user):
            return user == message.author and (str(reaction.emoji) == 'U1F638' or str(reaction.emoji) == 'U1F41D')
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=5.0, check=check)
            print('patata')
        except asyncio.TimeoutError:
            await canal.send('No has reaccionat amb un emoji de la llista')
        else:
            await canal.send('patata')
        '''print(reaccio)
        if reaccio == (':cat:'):
            await canal.send('Has escollit animals')
            #await channel.send(file=discord.File('ruta_fitxer.jpg'))
        elif reaccio == (':bee:'):
            await canal.send('Has escollit bichos')
            #await channel.send(file=discord.File('ruta_fitxer.jpg'))
        else:
            await canal.send('Aquesta reacció no es valida')'''
        
    #Galeta de la fortuna, utilitzant la llibrería "random" el bot escollirà una frase de l'array "frases" aleatoriament i la mostrarà per discord.
    if message.content.startswith('!fortuna'):
        canal = message.channel
        frases=[
            'Tendrás un día de alegrías y buenos momentos, disfrútalos como nunca.',
            'Concéntrate en lo que quieres lograr y ganaras. No lo olvides.',
            'El cielo sera tu limite, pues grandes acontecimientos te sucederán.',
            'Te sentirás feliz como un niño y veras al mundo con sus ojos.',
            'Vivirás tu vejez con comodidades y riquezas materiales.'
        ]
        await message.channel.send(random.choice(frases))
        
    #Comanda de prova per veure com enviar missatges per un canal de texte a Discord.
    if message.content.startswith('!patata'):
        canal = message.channel
        await canal.send('patata')
    #La seguent linea es la solució a que no s'executessin els @client.command, es degut a un conflicte amb els events on_message i aquesta es la sol·lució que he trovat.
    await client.process_commands(message)
    
################

#####COMANDES#####

#Comanda per entrar al canal de veu
@client.command(pass_context=True)
async def join(ctx):    
    channel = message.author.voice.voice_channel
    await client.join_channel(channel)


##################

#####TASKS#####

###############

client.run(token)
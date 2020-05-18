import discord
import random
import asyncio
import time
from discord.ext import commands, tasks

token = 'Njk5OTIyOTA4MTc2MzE4NTU5.Xqq8-g.C2Yvl3C6v1X19saiNDHyHJ6ZOOI'

client = commands.Bot(command_prefix='!')
client.remove_command('help')

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

#Comandes via events.
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
            return user == message.author and (str(reaction.emoji) == '\U0001f431' or str(reaction.emoji) == '\U0001f41d')
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
            #print(reaction)
        except asyncio.TimeoutError:
            await canal.send('No has reaccionat amb un emoji de la llista')
        else:
            #Si l'emoji es el gat, mostra una imatge d'un animal
            if str(reaction.emoji) == '\U0001f431':
                lista=[]
                for root, dirs, files in os.walk("./Imagenes/Animales"):
                    for filename in files:
                        lista.append(filename)
                imatgeamostrar=str(random.choice(lista)) #Guarda la imatge aleatoria a una variable per facil·litar utilitzarla en la seguent linea
                file = discord.File("./Imagenes/Animales/{}".format(imatgeamostrar), filename="image.png") # Estableix la variable que contindrá la imatge i el nom amb el que el bot la pujará.
                await canal.send(file=file)
            #Si l'emoji es l'abella, mostra una imatge d'un insecte
            elif str(reaction.emoji) == '\U0001f41d':
                lista=[]
                for root, dirs, files in os.walk("./Imagenes/Bichos"):
                    for filename in files:
                        lista.append(filename)
                imatgeamostrar=str(random.choice(lista)) #Guarda la imatge aleatoria a una variable per facil·litar utilitzarla en la seguent linea
                file = discord.File("./Imagenes/Bichos/{}".format(imatgeamostrar), filename="image.png") # Estableix la variable que contindrá la imatge i el nom amb el que el bot la pujará.
                await canal.send(file=file)
        
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
    
    #Comanda de prova
    if message.content.startswith('!test1'):
        canal = message.channel
        usuari = message.author
        await canal.send(usuari.mention)

    #Menciona a una persona aleatoria dintre del servidor.
    if message.content.startswith('!menciorandom'):
        canal = message.channel
        servidor = message.guild
        membresserver = servidor.members
        llistamembres =[]
        for i in membresserver:
            llistamembres.append(i.mention)
        await canal.send(random.choice(llistamembres))
    
    #Menciona a tothom dintre del servidor
    if message.content.startswith('!mencioall'):
        canal = message.channel
        servidor = message.guild
        membresserver = servidor.members
        for i in membresserver:
            await canal.send(i.mention)


    #La seguent linea es la solució a que no s'executessin els @client.command, es degut a un conflicte amb els events on_message i aquesta es la sol·lució que he trovat.
    await client.process_commands(message)
    
################

#####COMANDES#####

#Comanda d'ajuda que mostrarà totes les comandes disponibles del bot.
@client.command()
async def help(ctx):
    embed = discord.Embed()
    embed.set_author(name='Help')
    embed.add_field(name='----------------------------------------------------------------------------------------', value='Comandes de prova', inline=False)
    embed.add_field(name='!test1', value="Menciona a l'usuari que crida la comanda.", inline=False)
    embed.add_field(name='!eventest', value='Event de prova per veure com es poden fer comandes amb els events.', inline=False)
    embed.add_field(name='!patata', value='Comanda de prova per veure com enviar missatges per un canal de texte a Discord.', inline=False)
    embed.add_field(name='----------------------------------------------------------------------------------------', value='Comandes generals', inline=False)
    embed.add_field(name='!mencioall', value='Menciona a tothom en aquest servidor.', inline=False)
    embed.add_field(name='!menciorandom', value='Menciona aleatoriament a un usuari del servidor.', inline=False)
    embed.add_field(name='!imatge', value='Event/comanda que mostra una imatge dintre de la carpeta.', inline=False)
    embed.add_field(name='!fortuna', value="Galeta de la fortuna, utilitzant la llibrería 'random' el bot escollirà una frase de l'array 'frases' aleatoriament i la mostrarà per discord.", inline=False)
    embed.add_field(name='----------------------------------------------------------------------------------------', value='Comandes del canal de veu', inline=False)
    embed.add_field(name='!entrar', value="#Comanda per entrar al canal de veu, requereix d'un argument", inline=False)
    embed.add_field(name='!sortir', value='Comanda per sortir de qualsevol canal de veu', inline=False)
    await ctx.send(embed=embed)

#Comanda per fer un sorteig
@client.command()
async def sorteig(ctx, arg1, *, args):
    missatge = await ctx.send("Ha començat un sorteig de {} {}!\nReacciona a aquest missatge per entrar.".format(arg1, args))
    #Extraiem l'id del missatge del bot.
    canal = missatge.channel.id
    msg = missatge.id
    await missatge.add_reaction('\U0001F911')
    await asyncio.sleep(5)
    #Fem un refetch del missatge per actualitzar-lo a la caché i pdoer accedir a les reaccions afegides
    missatge2 = await client.get_channel(canal).fetch_message(msg)
    usuaris = []
    #Extraure totes les reaccions del missatge del bot
    for reaccio in missatge2.reactions:
        #Extraure tots els usuaris de les respectives reaccions
        async for usuari in reaccio.users():
            if usuari.id == 699922908176318559:
                pass
            else:
                usuaris.append(usuari.mention)
    guanyador = random.choice(usuaris)
    await ctx.send("El guanyador es {}!".format(guanyador))
    
    #print(missatge2.reactions)


#Comanda per entrar al canal de veu, requereix d'un argument
@client.command()
async def entrar(ctx, channel: discord.VoiceChannel):
    print(ctx.voice_client)
    #El seguent if verifica que si el bot està conectat a un servidor, en cas de que sí, en comptes de fer un connect farà un mobe_to
    if ctx.voice_client != None:
        await ctx.voice_client.move_to(channel)
    else:
        await channel.connect()

#Comanda per sortir de qualsevol canal de veu
@client.command()
async def sortir(ctx):
    await ctx.voice_client.disconnect()
##################

#####TASKS#####

###############

client.run(token)
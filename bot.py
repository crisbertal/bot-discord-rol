# incluye las funciones para conectarse con discord
import discord
# usada para los numeros al azar
import random

# toke de auth para el bot
TOKEN = 'NjkwOTYzNjI5NDAyNjIwMDA2.XnZjgg.Tezx3lcr2yoqLM2mxJn5KWM4OEg'

# inicia el cliente
client = discord.Client()


def frases_ciri():
    frases = [
        'Vamos a comer',
        'Vamos a desayunar',
        'Yo mato gente',
        'Matar',
    ]
    return frases[random.randint(0, len(frases) - 1)]


def frases_david():
    frases = [
        'Que te calles',
        'Matar matar',
        '¿Donde esta papa?',
    ]
    return frases[random.randint(0, len(frases) - 1)]


def d20():
    n = random.randint(1, 20)
    frases = [
        'Te echaremos de menos',
        'No esta mal, pero te van a reventar',
        'Lo has hecho bien, pero seguro que hay un asiatico mejor',
        'La culpa es de Zapatero',
        'Bastante bien, igual no te mueres',
        'Vas mamadisimo prro',
    ]
    if n == 1:
        return frases[0] + ' 💔 ' + str(n) + '️ 💔'
    elif n > 1 and n <= 5:
        return frases[1] + ' 🖤 ' + str(n) + '️ 🖤'
    elif n > 5 and n <= 10:
        return frases[2] + ' 🧡 ' + str(n) + ' ️🧡'
    elif n > 10 and n <= 15:
        return frases[3] + ' 💚 ' + str(n) + ' 💚'
    elif n > 15 and n <= 19:
        return frases[4] + ' ❤️ ' + str(n) + ' ❤️'
    else:
        return frases[5] + ' 💖 ' + str(n) + '️ 💖'


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/h'):
        await message.channel.send('Los comandos son:\n /di_frase,\n/bien,\n/iniciativa')

    if message.content.startswith('/di_frase'):
        await message.channel.send(frases_ciri())

    if message.content.startswith('/bien'):
        await message.channel.send('(hace ronroneo de pajaro)')

    if message.content.startswith('/i'):
        await message.channel.send(d20())

    if message.author.display_name == 'cndavid':
        await message.channel.send(frases_david())


# evento disparado cuando se realiza la conexion
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

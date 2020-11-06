import discord
import random

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

    fit = random.randint(1, 10)
    compatibility = random.randint(1, 101)

    elon_tweets = [
        'Technically, alcohol is a solution',
        'Tesla blows haha',
        'the color orange is named after the fruit',
        'We are literally a brain in a vat. The vat is your skull. Everything you think is real is an electrical '
        'signal. Feels so real though '
    ]
    eightball_responses = [
        'yes',
        'no',
        'very doubtful',
        'ask again later'
    ]
    commands = [
        'rate my fit',
        'elon tweet',
        '8ball + question + ?',
        'compatibility + @ person + !',
        'send cat',
        'send 70s bands',
        'send 80s bands',
        'send 90s bands',
    ]
    cat_pictures = [
        'https://imgur.com/f7hSxtF',
        'https://imgur.com/MAkb7J9',
        'https://imgur.com/aGXKQHV'
    ]
    seventies_bands = [
        'Led Zeppelin ' + 'https://imgur.com/dHEko3v',
        'The Rolling Stones ' + 'https://imgur.com/xvQqv6b',
        'Pink Floyd ' + 'https://imgur.com/23JWzI2',
        'Fleetwood Mac ' + 'https://imgur.com/DR3OEj9',
        'Chicago ' + 'https://imgur.com/2aqQY7W',
        'The Who ' + 'https://imgur.com/Vl0DAa3',
        'The Ramones ' + 'https://imgur.com/Q4MjOcy',
        'ABBA ' + 'https://imgur.com/8C5dCKe'
    ]
    eighties_bands = [
        'Guns N Roses ' + 'https://imgur.com/ab5KsxY',
        'Cinderella ' + 'https://imgur.com/RIl2JSv',
        'Twisted Sister ' + 'https://imgur.com/Xd2kSoH',
        'Motley Crue ' + 'https://imgur.com/bKXYaqe',
        'Whitesnake ' + 'https://imgur.com/lWyLIkZ',
        'Aerosmith ' + 'https://imgur.com/4t8hnSr',
        'Poison ' + 'https://imgur.com/P6fCKSG',
        'Queen ' + 'https://imgur.com/kEkxbuH'
    ]
    nineties_bands = [
        'Nirvana ' + 'https://imgur.com/Fp83poG',
        'Green Day ' + 'https://imgur.com/SWewsoM',
        'Blink-182 ' + 'https://imgur.com/OLW1pae',
        'Pearl Jam ' + 'https://imgur.com/VKqNG0q',
        'The Smashing Pumpkins ' + 'https://imgur.com/RHHKQK7',
        'Weezer ' + 'https://imgur.com/Aksal5d',
        'Red Hot Chili Peppers ' + 'https://imgur.com/3Ju0itG'
    ]

    # shows user commands
    if message.content == 'commands':
        await message.channel.send('\n'.join(map(str, commands)))

    # rates the user's outfit
    if message.content == 'rate my fit':
        await message.channel.send(str(fit) + '/10')

    # responds with a random elon musk tweet
    if message.content == 'elon tweet':
        response = random.choice(elon_tweets)
        await message.channel.send(response)

    # plays 8 ball
    if message.content.startswith('8ball') and message.content.endswith('?'):
        response = random.choice(eightball_responses)
        await message.channel.send(response)

    # sends cat pictures
    if message.content.startswith("send cat"):
        response = random.choice(cat_pictures)
        await message.channel.send(response)

    # sends pictures of bands from the 70s
    if message.content.startswith("send 70s bands"):
        response = random.choice(seventies_bands)
        await message.channel.send(response)

    # sends pictures of bands from the 80s
    if message.content.startswith("send 80s bands"):
        response = random.choice(eighties_bands)
        await message.channel.send(response)

    # sends pictures of bands from the 90s
    if message.content.startswith("send 90s bands"):
        response = random.choice(nineties_bands)
        await message.channel.send(response)

    if message.content.startswith('compatibility') and message.content.endswith('!'):
        await message.channel.send(str(compatibility) + '%')

client.run('hidden')

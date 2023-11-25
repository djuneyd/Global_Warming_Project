import discord
from discord.ext import commands
import uuid
import os
from AI_function import Mushroom
import requests

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send('===============================================================')
    await ctx.send('Привет! Я профессиональный грибник, различаю 20 видов грибов, а также могу сказать, съедобны они или нет. Ценную информацию о грибе вы также можете получить у меня. Для проверки гриба прикрепите фото гриба и напишите команду $check и я дам вам подробную информацию❗')
    await ctx.send('===============================================================')
    await ctx.send('Команда $baserules покажет вам базовые правила при обращении с грибами❗')
    await ctx.send('===============================================================')
    await ctx.send('Также я показываю максимально точный прогноз погоды любого города который вы пожелаете, для этого напишите команду $weather, потом название города и инициаллы страны на английском языке. Например: $weather Rome IT❗')
    await ctx.send('===============================================================')

@client.command()
async def weather(ctx, city, country):
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+', '+country+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
        weather_data = requests.get(url).json()
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        forecast = [city, str(temperature), str(temperature_feels)]

        await ctx.send('===============================================================')
        await ctx.send(f'Сейчас в городе {forecast[0]}: {forecast[1]} °C')
        await ctx.send(f'Ощущается как {forecast[2]} °C')
        await ctx.send('===============================================================')
    except:
        await ctx.send('===============================================================')
        await ctx.send('Пожалуйста, введите название города корректно❗')
        await ctx.send('===============================================================')

@client.command()
async def baserules(ctx):
    await ctx.send('===============================================================')
    await ctx.send('ПРАВИЛО №1:')
    await ctx.send('- собирать грибы следует вдали от дорог, магистралей, вне населенных мест, в экологически чистых районах. Собирать грибы лучше с восходом солнца, по росе')
    await ctx.send('ПРАВИЛО №2:')
    await ctx.send('- для сохранения свежести грибов необходимо собирать их в плетеную ивовую корзину. Не рекомендуется собирать в ведра, полиэтиленовые пакеты или мешки, так как в них нет доступа воздуха. Кроме того, в полиэтиленовых емкостях повышается температура, что приводит к порче грибов')
    await ctx.send('ПРАВИЛО №3:')
    await ctx.send('- нельзя собирать старые, переросшие, червивые и неизвестные грибы. Во время сбора нельзя пробовать грибы: употреблять их следует только после соответствующей термической обработки')
    await ctx.send('ПРАВИЛО №4:')
    await ctx.send('- нельзя брать грибы, имеющие утолщения у основания ножки. Чтобы не ошибиться в выборе грибов, необходимо их срезать с целой ножкой, чтобы дома еще раз проверить.')
    await ctx.send('ПРАВИЛО №5:')
    await ctx.send('- нельзя забывать, что некоторые съедобные грибы (опенок осенний, сыроежка) имеют ядовитых двойников.')
    await ctx.send('ВНИМАНИЕ!!!:')
    await ctx.send('- я точен не на сто  процентов и я не несу ни какой ответственности за предоставленную информацию')
    await ctx.send('===============================================================')


@client.command()
async def check(ctx):
    imageName = str(uuid.uuid4()) + '.jpg'
    await ctx.message.attachments[0].save(imageName)
    info = Mushroom(imageName)
    await ctx.send('===============================================================')
    await ctx.send(f'Тип: {info[0]}')
    await ctx.send(f'Вид: {info[1]}')
    await ctx.send(f'Шанс совпадения: {info[2] * 100}%')
    await ctx.send('===============================================================')
    await ctx.send('ВОТ НЕСКОЛЬКО ПРИМЕРОВ ИЗ МОЕГО ДАТА СЕТА❗')
    for i in range(4):
        with open(info[4][i], 'rb') as f:
            pic = discord.File(f)
        await ctx.send(file=pic)
    await ctx.send('===============================================================')
    await ctx.send('ЭТО ИНТЕРЕСНО❗')
    await ctx.send('=================')
    await ctx.send(info[3])
    await ctx.send('===============================================================')
    if info[0] == 'СЪЕДОБНЫЙ':
        await ctx.send(f'❗НА ЭТОМ САЙТЕ ТЫ НАЙДЁШЬ МНОГО ИНТЕРЕСНЫХ РЕЦЕПТОВ ИЗ СВОЕГО ГРИБА:❗')
        await ctx.send(info[5])
        await ctx.send('===============================================================')
    os.remove(imageName)


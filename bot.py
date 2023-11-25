import discord
from discord.ext import commands
import uuid
import os
# from AI_function import Tree
# from weather_function import weather
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
    await ctx.send('Привет! Я профессиональный ботаник, различаю 15 видов деревьев. Ценную информацию о дереве вы также можете получить у меня. Для проверки дерева прикрепите фото дерева и напишите команду $check и я дам вам подробную информацию❗ Также я выдаю максимально точный прогноз погоды из любого города которого вы только пожелаете❗ Для этого напишите команду $weather, потом название города и инициаллы страны!!!, Например: $weather Rome IT❗')
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

# @client.command()
# async def check(ctx):
#     imageName = str(uuid.uuid4()) + '.jpg'
#     await ctx.message.attachments[0].save(imageName)
#     info = Tree(imageName)
#     await ctx.send('===============================================================')
#     await ctx.send(f'Могу предположить что это: {info[0]}')
#     await ctx.send(f'Шанс моей уверенности: {info[1] * 100}%')
#     # await ctx.send('===============================================================')
#     # await ctx.send('ВОТ НЕСКОЛЬКО ПРИМЕРОВ ИЗ МОЕГО ДАТА СЕТА❗')
#     # for i in range(4):
#     #     with open(info[4][i], 'rb') as f:
#     #         pic = discord.File(f)
#     #     await ctx.send(file=pic)
#     await ctx.send('===============================================================')
#     await ctx.send('ЭТО ИНТЕРЕСНО❗')
#     await ctx.send('=================')
#     await ctx.send(info[2])
#     await ctx.send('===============================================================')
#     # await ctx.send(f'❗НА ЭТОМ САЙТЕ ТЫ НАЙДЁШЬ МНОГО ИНТЕРЕСНЫХ ФАКТОВ О ДЕРЕВЕ:❗')
#     # await ctx.send(info[5])
#     # await ctx.send('===============================================================')
#     os.remove(imageName)

client.run("MTE3Nzg3Mzc4MjAzMjA1NjM4MQ.GjJ_sp.z0hS4jfKYdCcsGbH_3970Zbkikfb33kGi_qySI")
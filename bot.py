import discord
from discord.ext import commands
import uuid
import os
from AI_function import Tree

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send('===============================================================')
    await ctx.send('Привет! Я профессиональный ботаник, различаю 20 видов деревьев. Ценную информацию о дереве вы также можете получить у меня. Для проверки дерева прикрепите фото дерева и напишите команду $check и я дам вам подробную информацию❗')
    await ctx.send('===============================================================')

@client.command()
async def check(ctx):
    imageName = str(uuid.uuid4()) + '.jpg'
    await ctx.message.attachments[0].save(imageName)
    info = Tree(imageName)
    await ctx.send('===============================================================')
    await ctx.send(f'Могу предположить что это: {info[0]}')
    await ctx.send(f'Шанс моей уверенности: {info[1] * 100}%')
    # await ctx.send('===============================================================')
    # await ctx.send('ВОТ НЕСКОЛЬКО ПРИМЕРОВ ИЗ МОЕГО ДАТА СЕТА❗')
    # for i in range(4):
    #     with open(info[4][i], 'rb') as f:
    #         pic = discord.File(f)
    #     await ctx.send(file=pic)
    await ctx.send('===============================================================')
    await ctx.send('ЭТО ИНТЕРЕСНО❗')
    await ctx.send('=================')
    await ctx.send(info[2])
    await ctx.send('===============================================================')
    # await ctx.send(f'❗НА ЭТОМ САЙТЕ ТЫ НАЙДЁШЬ МНОГО ИНТЕРЕСНЫХ ФАКТОВ О ДЕРЕВЕ:❗')
    # await ctx.send(info[5])
    # await ctx.send('===============================================================')
    os.remove(imageName)

        
client.run("MTE3NzY2NjE2MzE4MjkyODAyMw.GlbMet.rtsKWf6XfdBQOs_587d_io-dmJXmGVpSOygOmM")
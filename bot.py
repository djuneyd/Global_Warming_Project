import discord
from discord.ext import commands
from flask import redirect
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from main import Offers, db, app

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event 
async def on_message(message):

    if message.content.startswith('$hello'):
        await message.channel.send(f'Приветствую❗ Я бот помогающий борьбе с глобальным потеплением, если хочешь узнать мои функции, напиши команду ($help)❗')

    elif message.content.startswith('$help'):
        await message.channel.send(100*'-')
        await message.channel.send('''Команда ($offer) позволяет внести предложение в базу данных по борьбе с глобальным потеплением❗ --- Пример записи❗ ($offer не есть мясо)''')
        await message.channel.send(100*'-')

    elif message.content.startswith('$offer'):
        new = str(message.content).replace('$offer', '')
        if new != '':
            suggestion = Offers(offer=new)

            with app.app_context():
                db.session.add(suggestion)
                db.session.commit()
            await message.channel.send('Спасибо за помощь в сборе предложений❗ Мы записали вашу идею на наш официальный сайт❗')
        else:
            await message.channel.send('ПУСТОЕ ПРЕДЛОЖЕНИЕ ОТПРАВИТЬ НЕЛЬЗЯ❗')

client.run('MTE3MzMxMTgwOTk0MDM2NTMyMg.GgZhMd.YstvByw0utqi1KN9h0YfAbAah67HJdZyG3e6CE')
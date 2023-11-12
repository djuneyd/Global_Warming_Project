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
    if message.content.startswith('$offer'):
        new = str(message.content).replace('$offer', '')
        suggestion = Offers(offer=new)

        with app.app_context():
            db.session.add(suggestion)
            db.session.commit()
        await message.channel.send('Спасибо за помощь в сборе предложений! Мы записали вашу идею на наш официальный сайт!')




client.run('MTE3MzMxMTgwOTk0MDM2NTMyMg.Gkttxe.HsIRida-iOCALaVr8lazi3cNU9vMmMAIyfC6cQ')
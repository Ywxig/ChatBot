import discord
import CuteON
import sends
import Zoe
import BotHubAPI
import time
import Command_runer

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Загрузка систем..."))
        print("Добро пожаловать, Загрузка систем...")
        time.sleep(2)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Ассиастент Zoe 5.4"))
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == message.content:
            mes = (message.content).lower()
            mes_list = mes.split()
            try:
                await message.channel.send((Zoe.return_commad(mes_list)))
                await message.channel.send((Command_runer.start(mes_list)))
            except:
                print("ERR IN 'await message.channel.send((Zoe.return_commad(mes_list)))' ")

            channel = message.channel
            mess = message.content
            await message.channel.send(sends.main(mes_list))       

            return "Я не уверена в ответе"

        if message.content.startswith('.cls'):
            channel = message.channel
            messages = channel.history()
            await message.channel.send("Конечно, сейчас очищю!")
            async for message in messages:
                await message.delete()
                
intents = discord.Intents.all()
client = MyClient(intents=intents)

print(CuteON.Get_.getLine(file="Config.sws", nameString="Token"))
client.run(str(CuteON.Get_.getLine(file="Config.sws", nameString="Token")))

"""
print(BotHubAPI.Config.Get(name="Zoe"))
client.run(BotHubAPI.Config.Get(name="Zoe"))
"""
# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = "%", intents = intents)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
# 輸入%Hello呼叫指令
async def Hello(ctx: commands.Context):
    # 回覆Hello, world!
    await ctx.send("Hello, world!")

bot.run("BOT TOKEN")

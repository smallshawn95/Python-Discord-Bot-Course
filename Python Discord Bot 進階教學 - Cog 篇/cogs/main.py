import discord
from discord.ext import commands
# 導入core資料夾中的自寫模組
from core.classes import Cog_Extension

# 繼承Cog_Extension的self.bot物件
class Main(Cog_Extension):
    # 前綴指令
    @commands.command()
    async def Hello(self, ctx):
        await ctx.send("Hello, world!")
      
    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content == "Hello":
            await message.channel.send("Hello, world!")

# 載入cog中
async def setup(bot):
    await bot.add_cog(Main(bot))

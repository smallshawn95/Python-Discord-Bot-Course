from discord.ext import commands

# 繼承commands.Cog的指令工具
class Cog_Extension(commands.Cog):
    def __init__(self, bot: commands.Bot):
        # 讀取主程式中的bot物件
        self.bot = bot

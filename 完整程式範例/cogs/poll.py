import discord
from datetime import timedelta
from discord import app_commands
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="poll_base", description="投票基本")
    async def poll_base(self, interaction: discord.Interaction):
        # 宣告 Poll 類別，填入兩個必填參數
        poll = discord.Poll(
            question="晚餐吃什麼？",
            duration=timedelta(hours=1)
        )
        # 依序添加選項，text 和 emoji 參數自由選擇填寫
        poll.add_answer(text="漢堡王")
        poll.add_answer(text="丹丹漢堡")
        poll.add_answer(text="麥當勞", emoji="🍟")
        poll.add_answer(text="肯德基", emoji="🍗")
        await interaction.response.send_message(poll=poll)

    @app_commands.command(name="poll_multiple", description="投票複選")
    async def poll_multiple(self, interaction: discord.Interaction):
        # duration 參數設為 31 天後截止
        # multiple 參數設為 True 即可讓使用者複選選項
        poll = discord.Poll(
            question="舉辦哪個運動項目賽事",
            duration=timedelta(hours=31 * 24),
            multiple=True,
            layout_type=discord.PollLayoutType.default
        )
        poll.add_answer(text="籃球", emoji="🏀")
        poll.add_answer(text="排球", emoji="🏐")
        poll.add_answer(text="桌球", emoji="🏓")
        poll.add_answer(text="足球", emoji="⚽")
        poll.add_answer(text="棒球", emoji="⚾")
        poll.add_answer(text="壘球", emoji="🥎")
        poll.add_answer(text="撞球", emoji="🎱")
        poll.add_answer(text="網球", emoji="🎾")
        poll.add_answer(text="橄欖球", emoji="🏈")
        poll.add_answer(text="羽毛球", emoji="🏸")
        await interaction.response.send_message(poll=poll)

async def setup(bot: commands.Bot):
    await bot.add_cog(Poll(bot))

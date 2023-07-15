import time, discord, datetime
# 導入discord.ext模組中的tasks工具
from discord.ext import tasks, commands
from core.classes import Cog_Extension

class TaskBase(Cog_Extension):
    def __init__(self, bot):
        super().__init__(bot)
        # 開始執行函式
        self.hi.start()
        self.start_time = time.time()

    def cog_unload(self):
        # 取消執行函式
        self.hi.cancel()

    # 定義要執行的循環函式
    @tasks.loop(seconds = 1)
    async def hi(self):
        execution_time = int(time.time() - self.start_time)
        print(f"{execution_time}sec: Hello, world!")

class TaskAction(Cog_Extension):
    def __init__(self, bot):
        super().__init__(bot)
        self.action.start()

    @tasks.loop(seconds = 1)
    async def action(self):
        print("Action")
        self.action.cancel()

    # 執行函式前的動作
    @action.before_loop
    async def action_before(self):
        print("Wait")
        # 等待機器人上線完成
        await self.bot.wait_until_ready()

    # 結束執行函式後的動作
    @action.after_loop
    async def action_after(self):
        print("Stop")

class TaskCount(Cog_Extension):
    def __init__(self, bot):
        super().__init__(bot)
        self.count.start()
        self.start_time = time.time()

    # 循環三次，每五秒輸出執行第幾次
    @tasks.loop(seconds = 5, count = 3)
    async def count(self):
        execution_time = int(time.time() - self.start_time)
        print(f"{execution_time}sec: Count {self.count.current_loop}")

    # 函式執行三次後要執行的動作
    @count.after_loop
    async def after_slow_count(self):
        execution_time = int(time.time() - self.start_time)
        print(f"{execution_time}sec: Count end")

class TaskTime(Cog_Extension):
    # 臺灣時區 UTC+8
    tz = datetime.timezone(datetime.timedelta(hours = 8))
    # 設定每日十二點執行一次函式
    everyday_time = datetime.time(hour = 0, minute = 0, tzinfo = tz)

    def __init__(self, bot):
        super().__init__(bot)
        self.everyday.start()

    # 每日十二點發送 "晚安!瑪卡巴卡!" 訊息
    @tasks.loop(time = everyday_time)
    async def everyday(self):
        # 設定發送訊息的頻道ID
        channel_id = 1021706869724684376
        channel = self.bot.get_channel(channel_id)
        embed = discord.Embed(
            title = "🛏 晚安！瑪卡巴卡！",
            description = f"🕛 現在時間 {datetime.date.today()} 00:00",
            color = discord.Color.orange()
        )
        await channel.send(embed = embed)

class TaskTimes(Cog_Extension):
    # 設定整點執行一次函式
    every_hour_time = [
        datetime.time(hour = i, minute = 0, tzinfo = datetime.timezone(datetime.timedelta(hours = 8)))
        for i in range(24)
    ]

    def __init__(self, bot):
        super().__init__(bot)
        self.every_hour.start()

    # 每小時發送報時訊息
    @tasks.loop(time = every_hour_time)
    async def every_hour(self):
        # 設定發送訊息的頻道ID
        channel_id = 1021706869724684376
        channel = self.bot.get_channel(channel_id)
        embed = discord.Embed(
            title = f"⏰ 現在時間【{datetime.time.hour()}】時",
            color = discord.Color.random()
        )
        await channel.send(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(TaskBase(bot))
    await bot.add_cog(TaskAction(bot))
    await bot.add_cog(TaskCount(bot))
    await bot.add_cog(TaskTime(bot))
    await bot.add_cog(TaskTimes(bot))

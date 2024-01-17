import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")

# name指令名稱，description指令敘述
@bot.tree.command(name = "hello", description = "Hello, world!")
async def hello(interaction: discord.Interaction):
    # 回覆使用者的訊息
    await interaction.response.send_message("Hello, world!")

# @app_commands.describe(參數名稱 = 參數敘述)
# 參數: 資料型態，可以限制使用者輸入的內容
@bot.tree.command(name = "add", description = "計算相加值")
@app_commands.describe(a = "輸入數字", b = "輸入數字")
async def add(interaction: discord.Interaction, a: int, b: int):
    await interaction.response.send_message(f"Total: {a + b}")

# 參數: Optional[資料型態]，參數變成可選，可以限制使用者輸入的內容
@bot.tree.command(name = "say", description = "大聲說出來")
@app_commands.describe(name = "輸入人名", text = "輸入要說的話")
async def say(interaction: discord.Interaction, name: str, text: Optional[str] = None):
    if text == None:
        text = "。。。"
    await interaction.response.send_message(f"{name} 說 「{text}」")

# @app_commands.choices(參數 = [Choice(name = 顯示名稱, value = 隨意)])
@bot.tree.command(name = "order", description = "點餐機")
@app_commands.describe(meal = "選擇餐點", size = "選擇份量")
@app_commands.choices(
    meal = [
        Choice(name = "漢堡", value = "hamburger"),
        Choice(name = "薯條", value = "fries"),
        Choice(name = "雞塊", value = "chicken_nuggets"),
    ],
    size = [
        Choice(name = "大", value = 0),
        Choice(name = "中", value = 1),
        Choice(name = "小", value = 2),
    ]
)
async def order(interaction: discord.Interaction, meal: Choice[str], size: Choice[int]):
    # 獲取使用指令的使用者名稱
    customer = interaction.user.name
    # 使用者選擇的選項資料，可以使用name或value取值
    meal = meal.value
    size = size.value
    await interaction.response.send_message(f"{customer} 點了 {size} 號 {meal} 餐")

bot.run("BOT TOKEN")

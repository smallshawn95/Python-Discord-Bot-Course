import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")

@app_commands.command(name = "view_base", description = "簡單 View 範例")
async def view_base(interaction: discord.Interaction):
    # 創建一個 View，並設置 30 秒超時
    view = discord.ui.View(timeout = 30)
    # 添加一個 Button 到 View 中
    view.add_item(discord.ui.Button(label = "Button"))
    await interaction.response.send_message(view = view)

@app_commands.command(name = "view_class", description = "Class 版本 View 範例")
async def embed_class(interaction: discord.Interaction):
    # 創建一個 ViewClass 類別，並設置 30 秒超時
    view = ViewClass(timeout = 30)
    await interaction.response.send_message(view = view)

# 宣告一個 ViewClass 類別，繼承 discord.ui.View
class ViewClass(discord.ui.View):
    def __init__(self, timeout: float | None = 180):
        super().__init__(timeout = timeout)
        # 添加一個 Button 到 ViewClass 中
        self.add_item(discord.ui.Button(label = "Button"))

bot.run("BOT TOKEN")

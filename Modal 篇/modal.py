import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")

# 繼承 discord.ui.Modal 類別，並傳入 title 參數
class ModalClass(discord.ui.Modal, title = "設定名稱"):
    # 宣告一個 TextInput Item 元素
    name = discord.ui.TextInput(label = "Name")

    # Modal 提交後接著要執行的程式碼
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello, {self.name.value}!")

class ModalExample(discord.ui.Modal, title = "Modal 完整範例"):
    # placeholder 提示文字
    one = discord.ui.TextInput(label = "提示文字樣本", placeholder = "This is text.")
    # default 預設值
    two = discord.ui.TextInput(label = "預設值樣本", default = "This is text.")
    # min_length 文字最小長度
    three = discord.ui.TextInput(label = "文字最小長度", min_length = 10)
    # max_length 文字最大長度
    four = discord.ui.TextInput(label = "文字最大長度", max_length = 10)
    # style 風格和 required 必填取消
    five = discord.ui.TextInput(label = "風格和必填取消樣本", style = discord.TextStyle.paragraph, required = False)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{self.one}, {self.two}, {self.three}, {self.four}, {self.five}")

@bot.tree.command(name = "modal_base", description = "Modal 基本範例")
async def modal_base(interaction: discord.Interaction):
    # 回覆 Modal 給使用者
    await interaction.response.send_modal(ModalClass())

@bot.tree.command(name = "modal_example", description = "Modal 完整範例")
async def modal_example(interaction: discord.Interaction):
    await interaction.response.send_modal(ModalExample())

bot.run("BOT TOKEN")

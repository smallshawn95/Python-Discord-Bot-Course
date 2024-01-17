import discord, datetime
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")

@bot.tree.command(name = "embed_base", description = "初始 Embed")
async def embed_base(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "Discord Embed Teach",
        description = "這是一篇 Discord Embed 的教學文章",
        url = "https://hackmd.io/@smallshawn95/python_discord_bot_embed",
        color = discord.Color.blue(),
        timestamp = datetime.datetime.now()
    )
    await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "embed_thumbnail", description = "縮圖 Embed")
async def embed_thumbnail(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "Discord Embed Teach",
        description = "這是一篇 Discord Embed 的教學文章",
        color = discord.Color.blue()
    )
    embed.set_thumbnail(url = "https://i.imgur.com/BaBXr6b.png")
    await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "embed_author", description = "使用者 Embed")
async def embed_author(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "Discord Embed Teach",
        description = "這是一篇 Discord Embed 的教學文章",
        color = discord.Color.blue()
    )
    embed.set_author(name = interaction.user.name, url = interaction.user.avatar, icon_url = interaction.user.avatar)
    await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "embed_image", description = "圖片 Embed")
async def embed_image(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "Discord Embed Teach",
        description = "這是一篇 Discord Embed 的教學文章",
        color = discord.Color.blue()
    )
    embed.set_image(url = "https://i.imgur.com/fEowWaF.png")
    await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "embed_footer", description = "頁尾 Embed")
async def embed_footer(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "Discord Embed Teach",
        description = "這是一篇 Discord Embed 的教學文章",
        color = discord.Color.blue()
    )
    embed.set_footer(text = interaction.user.name, icon_url = interaction.user.avatar)
    await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "embed_field", description = "欄位 Embed")
async def embed_field(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "Discord Embed Teach",
        description = "這是一篇 Discord Embed 的教學文章",
        color = discord.Color.blue()
    )
    embed.add_field(name = "Discord Embed", value = "")
    embed.add_field(name = "Discord Embed", value = "")
    await interaction.response.send_message(embed = embed)

bot.run("BOT TOKEN")

import discord
import datetime
from discord.ext import commands
from discord import app_commands
from core.classes import Cog_Extension

class Embed(Cog_Extension):
    @app_commands.command(name = "embed", description = "完整 Embed")
    async def embed(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = "Discord Embed Teach",
            description = "這是一篇 Discord Embed 的教學文章",
            url = "https://hackmd.io/@smallshawn95/python_discord_bot_embed",
            color = discord.Color.blue(),
            timestamp = datetime.datetime.now()
        )
        embed.set_thumbnail(url = "https://i.imgur.com/BaBXr6b.png")
        embed.set_author(name = interaction.user.name, url = interaction.user.avatar, icon_url = interaction.user.avatar)
        embed.set_image(url = "https://i.imgur.com/fEowWaF.png")
        embed.set_footer(text = interaction.user.name, icon_url = interaction.user.avatar)
        embed.add_field(name = "😶 SmallShawn95", value = "https://smallshawn95.github.io/", inline = False)
        await interaction.response.send_message(embed = embed)

    @app_commands.command(name = "embed_base", description = "初始 Embed")
    async def embed_base(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = "Discord Embed Teach",
            description = "這是一篇 Discord Embed 的教學文章",
            url = "https://hackmd.io/@smallshawn95/python_discord_bot_embed",
            color = discord.Color.blue(),
            timestamp = datetime.datetime.now()
        )
        await interaction.response.send_message(embed = embed)

    @app_commands.command(name = "embed_thumbnail", description = "縮圖 Embed")
    async def embed_thumbnail(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = "Discord Embed Teach",
            description = "這是一篇 Discord Embed 的教學文章",
            color = discord.Color.blue()
        )
        embed.set_thumbnail(url = "https://i.imgur.com/BaBXr6b.png")
        await interaction.response.send_message(embed = embed)

    @app_commands.command(name = "embed_author", description = "使用者 Embed")
    async def embed_author(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = "Discord Embed Teach",
            description = "這是一篇 Discord Embed 的教學文章",
            color = discord.Color.blue()
        )
        embed.set_author(name = interaction.user.name, url = interaction.user.avatar, icon_url = interaction.user.avatar)
        await interaction.response.send_message(embed = embed)

    @app_commands.command(name = "embed_image", description = "圖片 Embed")
    async def embed_image(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = "Discord Embed Teach",
            description = "這是一篇 Discord Embed 的教學文章",
            color = discord.Color.blue()
        )
        embed.set_image(url = "https://i.imgur.com/fEowWaF.png")
        await interaction.response.send_message(embed = embed)

    @app_commands.command(name = "embed_footer", description = "頁尾 Embed")
    async def embed_footer(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = "Discord Embed Teach",
            description = "這是一篇 Discord Embed 的教學文章",
            color = discord.Color.blue()
        )
        embed.set_footer(text = interaction.user.name, icon_url = interaction.user.avatar)
        await interaction.response.send_message(embed = embed)

    @app_commands.command(name = "embed_field_yes", description = "同行欄位 Embed")
    async def embed_field_yes(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = "Discord Embed Teach",
            description = "這是一篇 Discord Embed 的教學文章",
            color = discord.Color.blue()
        )
        embed.add_field(name = "Discord Embed", value = "Discord Embed", inline = True)
        embed.add_field(name = "😶 SmallShawn95", value = "https://smallshawn95.github.io/", inline = True)
        await interaction.response.send_message(embed = embed)

    @app_commands.command(name = "embed_field_no", description = "不同行欄位 Embed")
    async def embed_field_no(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = "Discord Embed Teach",
            description = "這是一篇 Discord Embed 的教學文章",
            color = discord.Color.blue()
        )
        embed.add_field(name = "Discord Embed", value = "Discord Embed", inline = False)
        embed.add_field(name = "😶 SmallShawn95", value = "https://smallshawn95.github.io/", inline = False)
        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Embed(bot))

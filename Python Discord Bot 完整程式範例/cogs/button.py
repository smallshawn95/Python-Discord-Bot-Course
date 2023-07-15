import discord
from discord.ext import commands
from discord import app_commands
from core.classes import Cog_Extension

# 創建按鈕交互函式
async def button_callback(interaction: discord.Interaction):
    await interaction.response.edit_message(content = "Hello, world!")

# 創建自定 View
class ButtonView(discord.ui.View):
    def __init__(self, timeout: float | None = 180):
        super().__init__(timeout = timeout)

    @discord.ui.button(
        label = "Click",
        style = discord.ButtonStyle.blurple
    )
    async def button_decorator(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content = "Hello, world!")

class Button(Cog_Extension):
    # 回呼函式(Callback)
    @app_commands.command(name = "button_interaction_callback", description = "Button 回呼函式交互")
    async def button_interaction_callback(self, interaction: discord.Interaction):
        view = discord.ui.View()
        button = discord.ui.Button(
            label = "Click",
            style = discord.ButtonStyle.blurple
        )
        button.callback = button_callback
        view.add_item(button)
        await interaction.response.send_message(view = view)

    # 被裝飾函式(Decorator)
    @app_commands.command(name = "button_interaction_decorator", description = "Button 被裝飾函式交互")
    async def button_interaction_decorator(self, interaction: discord.Interaction):
        view = ButtonView()
        await interaction.response.send_message(view = view)

    # 持續監聽事件(Event Listener)
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if "custom_id" in interaction.data:
            if interaction.data["custom_id"] == "hello_world":
                await interaction.response.edit_message(content = "Hello, world!")

    @app_commands.command(name = "button_interaction_on", description = "Button 持續監聽事件交互")
    async def button_interaction_on(self, interaction: discord.Interaction):
        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label = "Hello, world!",
                style = discord.ButtonStyle.blurple,
                custom_id = "hello_world"
            )
        )
        await interaction.response.send_message(view = view)

    @app_commands.command(name = "button_style", description = "所有 Button 風格")
    async def button_style(self, interaction: discord.Interaction):
        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label = "Primary",
                style = discord.ButtonStyle.primary,
                row = 0
            )
        )
        view.add_item(
            discord.ui.Button(
                label = "Blurple",
                style = discord.ButtonStyle.blurple,
                row = 0
            )
        )
        view.add_item(
            discord.ui.Button(
                label = "Secondary",
                style = discord.ButtonStyle.secondary,
                row = 1
            )
        )
        view.add_item(
            discord.ui.Button(
                label = "Grey",
                style = discord.ButtonStyle.grey,
                row = 1
            )
        )
        view.add_item(
            discord.ui.Button(
                label = "Gray",
                style = discord.ButtonStyle.gray,
                row = 1
            )
        )
        view.add_item(
            discord.ui.Button(
                label = "Success",
                style = discord.ButtonStyle.success,
                row = 2
            )
        )
        view.add_item(
            discord.ui.Button(
                label = "Green",
                style = discord.ButtonStyle.green,
                row = 2
            )
        )
        view.add_item(
            discord.ui.Button(
                label = "Danger",
                style = discord.ButtonStyle.danger,
                row = 3
            )
        )
        view.add_item(
            discord.ui.Button(
                label = "Red",
                style = discord.ButtonStyle.red,
                row = 3
            )
        )
        view.add_item(
            discord.ui.Button(
                label = "link",
                style = discord.ButtonStyle.link,
                url = "https://hackmd.io/@smallshawn95/python_discord_bot_button",
                row = 4
            )
        )
        view.add_item(
            discord.ui.Button(
                label = "Url",
                style = discord.ButtonStyle.url,
                url = "https://hackmd.io/@smallshawn95/python_discord_bot_button",
                row = 4
            )
        )
        await interaction.response.send_message(view = view)

async def setup(bot: commands.Bot):
    await bot.add_cog(Button(bot))

import discord
from typing import List, Union
from discord.ext import commands

class Event(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 機器人加入伺服器
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        print(f"Bot 加入「{guild.name}」伺服器")

    # 機器人離開伺服器
    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        print(f"Bot 離開「{guild.name}」伺服器")

    # 伺服器更新
    @commands.Cog.listener()
    async def on_guild_update(self, before: discord.Guild, after: discord.Guild):
        if before.name != after.name:
            print(f"伺服器更新名稱「{before.name} -> {after.name}」")

    # 成員加入
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        print(f"「{member.display_name}」加入「{member.guild.name}」伺服器")

    # 成員離開
    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        print(f"「{member.display_name}」離開「{member.guild.name}」伺服器")

    # 成員封禁
    @commands.Cog.listener()
    async def on_member_ban(guild: discord.Guild, user: discord.User):
        print(f"「{guild.name}」伺服器 Ban「{user.display_name}」")

    # 成員解禁
    @commands.Cog.listener()
    async def on_member_unban(guild: discord.Guild, user: discord.User):
        print(f"「{guild.name}」伺服器 UnBan「{user.display_name}」")

    # 發送訊息
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        print(f"「{message.author.display_name}」發送訊息「{message.content}」")

    # 更改訊息
    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        print(f"「{before.author.display_name}」更改訊息「{before.content} -> {after.content}」")

    # 刪除訊息
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        print(f"「{message.author.display_name}」刪除訊息「{message.content}」")

    # 添加反應
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: Union[discord.Member, discord.User]):
        print(f"「{user.display_name}」添加反應「{reaction.emoji}」到「{reaction.message.content}」訊息")

    # 移除反應
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction: discord.Reaction, user: Union[discord.Member, discord.User]):
        print(f"「{user.display_name}」移除反應「{reaction.emoji}」到「{reaction.message.content}」訊息")

    # 清空反應
    @commands.Cog.listener()
    async def on_reaction_clear(self, message: discord.Message, reaction: List[discord.Reaction]):
        reaction = [str(i.emoji) for i in reaction]
        print(f"訊息「{message.content}」移除所有反應「{', '.join(reaction)}」")

    # 監聽交互作用
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        print(f"「{interaction.user.display_name}」使用「/{interaction.command.name}」指令")

    # 監聽語音動作
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if before.channel is None and after.channel:
            print(f"「{member.display_name}」加入「{after.channel.name}」語音頻道")
        elif before.channel and after.channel is None:
            print(f"「{member.display_name}」離開「{before.channel.name}」語音頻道")
        elif before.channel != after.channel:
            print(f"「{member.display_name}」移動「{before.channel.name} -> {after.channel.name}」語音頻道")

async def setup(bot: commands.Bot):
    await bot.add_cog(Event(bot))

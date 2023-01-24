import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.command()
async def unban(ctx, user_id: int = None, *, reason: str = None):
    if user_id is None:
        await ctx.send(f"{ctx.author.mention},الرجاء ادخال id المستخدم")
        return
    # Check if the user has the ban_members permission
    if not ctx.message.author.guild_permissions.ban_members:
        await ctx.send(f"{ctx.author.mention},ليس لديك الصلاحيات الازمه")
        return
    guild = ctx.guild
    await guild.unban(discord.Object(id=user_id), reason=reason)
    await ctx.send(f"العضو هذا {user_id} تم رفع الحضر عنه")

bot.run("Token_Bot_here")
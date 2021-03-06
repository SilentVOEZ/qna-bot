# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord, datetime, time
import psutil
from discord.ext import commands

start_time = time.time()

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

# Status Cycle
    @commands.command()
    @commands.is_owner()
    async def online(self, ctx, *, cactivity = ""):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f'{cactivity}', type=3))

    @commands.command()
    @commands.is_owner()
    async def idle(self, ctx, *, cactivity = ""):
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f'{cactivity}', type=3))

    @commands.command()
    @commands.is_owner()
    async def dnd(self, ctx, *, cactivity = ""):
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=f'{cactivity}', type=3))

# Utility
    @commands.command(pass_context=True)
    async def status(self, ctx):
        # Time
        current_time = time.time()
        difference = int(round(current_time - start_time))
        utime = str(datetime.timedelta(seconds=difference))

        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        # PSUtil - RAM Usage
        dict(psutil.virtual_memory()._asdict())
        usedmem = psutil.virtual_memory().used/1024/1024
        # activemem = psutil.virtual_memory().active
        tmem = psutil.virtual_memory().total/1024/1024
        pmem = round((usedmem/tmem)*100)

        # PSUtil - Swap Memory Usage
        # dict(psutil.swap_memory()._asdict())
        # uswap = psutil.swap_memory().used/1024/1024
        # tswap = psutil.swap_memory().total/1024/1024
        # pswap = round((uswap/tswap)*100)

        # PSUtil Operating System
        if psutil.LINUX:
            os = 'Linux'
        elif psutil.MACOS:
            os = 'MacOS'
        elif psutil.WINDOWS:
            os = 'Windows'
        else:
            os = 'Unknown'
        embed.set_author(name='System Monitor')
        embed.add_field(name="CPU Usage", value=f'{psutil.cpu_percent()}%', inline=True)
        embed.add_field(name="CPU Cores", value=psutil.cpu_count(), inline=True)
        embed.add_field(name="RAM Usage", value=f'{round(usedmem)}/{round(tmem)}MB ({round(pmem)}%)', inline=True)
        # embed.add_field(name="Swap Usage", value=f'{round(uswap)}/{round(tswap)}MB ({round(pmem)}%)', inline=True)
        embed.add_field(name="Uptime", value=f'{utime}', inline=True)
        embed.add_field(name="Operating System", value=os, inline=True)
        embed.set_footer(text="Bot by SilentVOEZ")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utility(bot))
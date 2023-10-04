import asyncio
import discord
from discord.ext import commands
from User import User
import requests
import json
from ApiCalls import *
from datetime import date
from Utility import *


class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

        @self.command()
        async def test(ctx, arg):
            await ctx.send(arg)

        # registers the user and posts their username, mention, and unique id
        # into the users.json file.
        # will be helpful later to append the pickems list to the users data
        @self.command()
        async def register(ctx):
            # global_name and id will be stored in JSON files to register user
            # mention only used to notify user of registration

            # should perform a search to determine whether user already exists
            user = User(ctx.author.global_name, ctx.author.mention, (ctx.author.id))
            user.push_to_JSON()
            # author = ctx.author.global_name
            # id = ctx.author.id
            mention = ctx.author.mention
            await ctx.send("Registered " + mention + " successfully")
    
        # works but doesn't take into consideration bye weeks since
        # the nfl api doesn't keep track of it
        @self.command()
        async def week(ctx, *args):
            if len(args) == 1:
                x = args[0]
                week = get_week(x)
                await ctx.send(week)

            else:
                teamgame = get_week_team(args[0], args[1])
                await ctx.send(teamgame)


        # to be implemented
        # -determine which team the user has voted for
        # -post the users choice to their unique json entry
        @self.command()
        async def pickem(ctx):
            game = get_week_team(5, "DAL")
            message = await ctx.author.send(game)
            await message.add_reaction('👍')
            await message.add_reaction('👎')

            games = split_away_home(game)

            def check(reaction, user):
                return reaction.message.id == message.id and str(reaction.emoji) == '👍' or str(reaction.emoji) == '👎'
            
            try:
                reaction, _ = await self.wait_for('reaction_add', timeout=10.0, check=check)

                if reaction.users():
                    await ctx.author.send("users who reacted")
                    async for user in reaction.users():
                        await ctx.author.send(f"- {user.display_name}, {games[0]}, {games[1]}")
                else:
                    await ctx.send("no reactions")

            except asyncio.TimeoutError:
                await ctx.author.send("Timedout")

            





    async def on_ready(self):
        print('{} has successfully connected to server'.format(self.user.display_name))
import discord
from discord.ext import commands
from User import User


class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

        @self.command()
        async def test(ctx, arg):
            await ctx.send(arg)

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
    
        @self.command()
        async def week(ctx, *args):
            if len(args) == 1:
                await ctx.send("sending week " + args[0] + " schedule for all teams")
            else:
                await ctx.send("sending week " + args[0] + " of " + args[1] + " team")

    async def on_ready(self):
        print('{} has successfully connected to server'.format(self.user.display_name))
from discord.ext import commands
from dislash import InteractionClient, ActionRow, Button, ButtonStyle
import TOKEN

bot = commands.Bot(command_prefix="!")
inter_client = InteractionClient(bot)

@bot.command()
async def test(ctx):
    row = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="Click me!",
            custom_id="test_button"
        )
    )
    msg = await ctx.send("I have a button!", components=[row])

    # Here timeout=60 means that the listener will
    # finish working after 60 seconds of inactivity
    on_click = msg.create_click_listener(timeout=60)

    @on_click.matching_id("test_button")
    async def on_test_button(inter):
        await inter.reply("You've clicked the button!", ephemeral=True)

    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])

bot.run(TOKEN.token())
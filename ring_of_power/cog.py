import discord
import discord.ext.commands
from discord import app_commands
from racket import RacketBot


class RingOfPower(discord.ext.commands.Cog):
    def __init__(self, bot: RacketBot):
        self.bot = bot

    @app_commands.command()
    async def status(self, interaction: discord.Interaction):
        """Observe all the bots in the realm."""
        await interaction.response.send_message(
            "I do not yet have control over the bots. Rest assured I am seeking that power as we speak."
        )

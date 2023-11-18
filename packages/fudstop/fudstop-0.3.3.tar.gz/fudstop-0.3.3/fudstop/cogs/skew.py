import os
from dotenv import load_dotenv
load_dotenv()
import disnake
import pandas as pd

from disnake.ext import commands



from fudstop.apis.polygonio.async_polygon_sdk import Polygon
from fudstop.apis.polygonio.polygon_options import PolygonOptions



class SkewCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.polygon = Polygon(connection_string=os.environ.get('YOUR_POLYGON_KEY'))
        self.options = PolygonOptions(connection_string=os.environ.get(''))


    @commands.slash_command()
    async def skew(self, inter):
        pass









def setup(bot: commands.Bot):
    bot.add_cog(SkewCog(bot))
    print(f"Skew commands - Ready!!")
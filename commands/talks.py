from discord.ext import commands
import discord


class Talks(commands.Cog):
    """Talks with user"""

    def __init__(self, bot):
        self.bot = bot

    # bot.command => commands.command
    @commands.command(name="oi", help="Envia um Oi (Não requer argumento)")
    async def send_hello(self, ctx):

        response = "E aí? Tudo bem??"

        await ctx.send(response)

    @commands.command(
        name="segredo", help="Envia um segredo no privado. Não requer argumento"
    )
    async def secret(self, ctx):
        try:
            await ctx.author.send("Grandes coisas virão...")
            await ctx.author.send("A idade da Terra é de 4,54 milhões de anos")
            await ctx.author.send(
                "Em breve"
            )
        except discord.errors.Forbidden:
            await ctx.send(
                "Não posso te contar o segredo! Por favor, habilite em (Opções > Privacidade)"
            )


def setup(bot):
    bot.add_cog(Talks(bot))

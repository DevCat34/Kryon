# ---------------- ICON SERVER ----------------

@tree.command(
    name="icon-server",
    description="Muestra el icono del servidor"
)
async def cmd_icon_server(
    interaction: discord.Interaction
):

    if not interaction.guild.icon:

        return await interaction.response.send_message(
            "❌ Este servidor no tiene icono.",
            ephemeral=True
        )

    embed = discord.Embed(
        title=f"🖼️ Icono de {interaction.guild.name}",
        color=discord.Color.blue()
    )

    embed.set_image(
        url=interaction.guild.icon.url
    )

    await interaction.response.send_message(
        embed=embed
    )
     # IMPORTANTE: Usar todos los imports establecidos en el archivo "imports.py"
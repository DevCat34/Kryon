# ---------------- AVATAR ----------------

@tree.command(
    name="avatar",
    description="Muestra el avatar de un usuario"
)
@app_commands.describe(
    usuario="Usuario del que quieres ver el avatar"
)
async def cmd_avatar(
    interaction: discord.Interaction,
    usuario: discord.Member = None
):

    usuario = usuario or interaction.user

    embed = discord.Embed(
        title=f"🖼️ Avatar de {usuario}",
        color=discord.Color.blue()
    )

    embed.set_image(
        url=usuario.display_avatar.url
    )

    embed.set_footer(
        text=f"ID: {usuario.id}"
    )

    await interaction.response.send_message(
        embed=embed
    )
    # IMPORTANTE: Usar todos los imports establecidos en el archivo "imports.py"
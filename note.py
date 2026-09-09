# 1. Örnek Slash Komutu: /ping
@bot.tree.command(name="ping", description="Botun çalışıp çalışmadığını test eder.")
async def ping(interaction: discord.Interaction):
    # Slash komutlarında ctx yerine interaction kullanılır
    await interaction.response.send_message("Pong! 🏓")


# 2. Örnek Slash Komutu: Parametreli /selam
@bot.tree.command(name="selam", description="Belirtilen kullanıcıya selam verir.")
@app_commands.describe(kullanici="Selam vermek istediğiniz kişi")
async def selam(interaction: discord.Interaction, kullanici: discord.User):
    await interaction.response.send_message(f"Merhaba {kullanici.mention}!")
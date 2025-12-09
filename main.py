from urllib.parse import urlparse
import discord
from discord.ext import commands
import os 
from dotenv import load_dotenv

from install_videos import baixar_video
from post_video_yt import postar_youtube

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# ID do canal
ID_DO_CANAL_MONITORADO = 1447961307394609273 

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

DOMINIOS_PERMITIDOS = {"youtube.com", "youtu.be","medal.tv", }

def link_validated(url: str) -> bool:
    try:
        dominio = urlparse(url).netloc.lower()
        return dominio in DOMINIOS_PERMITIDOS
    except Exception:
        return False


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == ID_DO_CANAL_MONITORADO:
        print(f"Nova mensagem detectada no canal monitorado: {message}")
        is_validated = link_validated(message.content)

        if(is_validated):
            try:
                video = await baixar_video(message.content)
                url = await postar_youtube(video)
                await message.channel.send(f"Vídeo postado com sucesso!: {url}")

            except Exception as e:
                await message.channel.send(f"Erro ao postar conteúdo {e}")
            
            arquivos = ["video.mp4", "post.mp4"]
            for arquivo in arquivos:
                try:
                    if os.path.exists(arquivo):
                        os.remove(arquivo)
                        print(f"Deletado: {arquivo}")
                except Exception as e:
                    print(f"Erro ao deletar {arquivo}: {e}")

        else:
            await message.channel.send("Não é um link válido")

    await bot.process_commands(message)
bot.run(TOKEN)

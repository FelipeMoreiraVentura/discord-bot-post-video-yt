import yt_dlp
import subprocess


async def baixar_video_yt(url: str):
    opts = {
        "format": "mp4/bv*+ba/b",
        "outtmpl": "video.%(ext)s",
        "merge_output_format": "mp4",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "http_headers": {
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
            "Connection": "keep-alive",
        },
        "retries": 10,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "socket_timeout": 30,
        "verbose": True,
    }

    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)

    return info.get("title", " ")




async def converter_resolucao(input_video="video.mp4", output_video="post.mp4"):
    comando = [
        "ffmpeg",
        "-i", input_video,
        "-vf",
        "scale=1080:-1:force_original_aspect_ratio=decrease,"
        "pad=1080:1920:(1080-iw)/2:(1920-ih)/2",
        "-c:a", "copy",
        "-preset", "fast",
        output_video
    ]

    subprocess.run(comando)

async def baixar_video(url: str):
    if "medal.tv" in url or "youtube.com" in url or "youtu.be" in url:
        titulo = await baixar_video_yt(url)
    else:
        raise ValueError("Plataforma não suportada.")

    await converter_resolucao()
    return titulo

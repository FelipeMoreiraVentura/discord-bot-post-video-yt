# 🎥 discord-bot-post-video-yt
Bot do Discord que baixa vídeos de YouTube ou Medal.tv, converte para formato vertical e posta automaticamente no YouTube.

---

## 🚀 Como rodar?

---

## 1️⃣ Criar e ativar um ambiente virtual

### **Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

---

## 2️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

---

## 3️⃣ Criar seu bot no Discord

Acesse o Discord Developer Portal e siga a documentação oficial para criar um bot e obter o token:  
https://discord.com/developers/docs/intro

Crie um arquivo `.env` na raiz do projeto:

```
DISCORD_TOKEN=SEU_TOKEN_AQUI
```

---

## 4️⃣ Criar credenciais para upload no YouTube

Acesse o Google Cloud Console e siga a documentação oficial para configurar OAuth e habilitar a YouTube Data API v3:  
https://developers.google.com/youtube/v3

Baixe o arquivo `client_secret.json` e coloque na raiz do projeto.

Na primeira execução o bot criará automaticamente `token.json`.

---

## 5️⃣ Executar o bot
```bash
python main.py
```

---

## 📌 Funcionamento do bot
- Monitora um canal específico do Discord  
- Ao detectar um link do **YouTube** ou **Medal.tv**, o bot:
  1. Baixa o vídeo usando **yt-dlp**
  2. Converte para formato vertical 1080x1920 com **FFmpeg**
  3. Publica automaticamente no YouTube
  4. Envia a URL do vídeo postado no chat do Discord
  5. Remove arquivos temporários (`video.mp4` e `post.mp4`)

---

## 🧰 Pré-requisitos
- Python 3.10+
- FFmpeg instalado no sistema  
  Verifique com:
  ```bash
  ffmpeg -version
  ```
- Conta no Discord Developer Portal
- Projeto no Google Cloud com YouTube Data API habilitada

---

## 🛠 Tecnologias usadas
- discord.py  
- yt-dlp  
- FFmpeg  
- YouTube Data API v3  
- OAuth2 Google  

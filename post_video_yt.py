from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import os

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def autenticar_youtube():
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


async def postar_youtube(titulo):
    creds = autenticar_youtube()
    youtube = build("youtube", "v3", credentials=creds)

    upload = MediaFileUpload("post.mp4", chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": titulo,
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=upload
    )

    response = request.execute()
    video_id = response.get("id")
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    return video_url
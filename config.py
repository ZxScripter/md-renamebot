import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", "26376042"))
    API_HASH = os.environ.get("API_HASH" "1f5343b0646645ca1eaf7c4759fc248f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6549833188:AAH5aUU_uNsJE8I4EPf98DxDUV5UTEtYCt4"
    OWNER_ID = int(os.environ.get("OWNER_ID", "2036803347"))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1001934076980)
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://userbot:userbot@cluster0.ltasu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

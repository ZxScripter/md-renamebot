import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", "26376042"))
    API_HASH = os.environ.get("API_HASH" "1f5343b0646645ca1eaf7c4759fc248f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6503352676:AAFdmZZWiFSpyLwuTOldk-QD6hSZXrX-y5M")
    OWNER_ID = int(os.environ.get("OWNER_ID", "2036803347"))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1001918398170")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://userbot:userbot@cluster0.ltasu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

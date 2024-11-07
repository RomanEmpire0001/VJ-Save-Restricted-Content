import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25873811"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "db68f02853eb8df7d234777a0888d02c")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://RomanEmpire:84A7PM3o6C6xznB1@cluster0.dmkh5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

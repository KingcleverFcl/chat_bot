import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

if not BOT_TOKEN or not DATABASE_URL:
    raise EnvironmentError("BOT_TOKEN и DATABASE_URL должны быть заданы в переменных окружения Railway")

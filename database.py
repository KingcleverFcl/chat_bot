import asyncpg
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# Устанавливаем соединение с базой
async def get_connection():
    return await asyncpg.connect(DATABASE_URL)

import asyncio
from database import get_connection

async def main():
    conn = await get_connection()

    # Пример запроса
    rows = await conn.fetch("SELECT NOW();")
    print(rows)

    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())

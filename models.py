from sqlalchemy import Table, Column, String, Integer, DateTime, MetaData, Text

metadata = MetaData()

users = Table("users", metadata,
    Column("telegram_id", String, primary_key=True),
    Column("nickname", String, unique=True),
    Column("date", DateTime),
)

messages = Table("messages", metadata,
    Column("id", Integer, primary_key=True),
    Column("sender_telegram_id", String),
    Column("recipient_telegram_id", String),
    Column("message", Text),
    Column("date", DateTime),
    Column("when_read", DateTime, nullable=True),
)

chats = Table("chats", metadata,
    Column("telegram_id_user1", String),
    Column("telegram_id_user2", String),
    Column("messages_user1", Text),
    Column("messages_user2", Text),
)

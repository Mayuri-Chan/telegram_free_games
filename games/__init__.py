import os

# Postgresql
from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

ENV = os.environ.get("ENV", False)
if ENV:
	API_ID = os.environ.get("API_ID", None)
	API_HASH = os.environ.get("API_HASH", None)
	BOT_SESSION = os.environ.get("BOT_SESSION", None)
	DATABASE_URL = os.environ.get("DATABASE_URL", None)
	WORKERS = int(os.environ.get("WORKERS", 6))
	GAME_CHAT = os.environ.get("GAME_CHAT", None)
	TZ = os.environ.get("TZ", "Asia/Jakarta")
	INTERVAL = os.environ.get("INTERVAL", 30*60)
else:
	from games.config import Config
	config = Config()
	API_ID = config.API_ID
	API_HASH = config.API_HASH
	BOT_SESSION = config.BOT_SESSION
	DATABASE_URL = config.DATABASE_URL
	WORKERS = config.WORKERS
	GAME_CHAT = config.GAME_CHAT
	TZ = config.TZ
	INTERVAL = config.INTERVAL

DB_AVAILABLE = False

# Postgresql
def mulaisql() -> scoped_session:
	global DB_AVAILABLE
	engine = create_engine(DATABASE_URL, client_encoding="utf8")
	BASE.metadata.bind = engine
	try:
		BASE.metadata.create_all(engine)
	except exc.OperationalError:
		DB_AVAILABLE = False
		return False
	DB_AVAILABLE = True
	return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = mulaisql()

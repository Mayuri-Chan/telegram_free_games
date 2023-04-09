class Config(object):
	API_ID = 12345 # from my.telegram.org
	API_HASH = "12345abcdef" # from my.telegram.org
	BOT_SESSION = "" # generate using session_maker.py
	DATABASE_URL = "postgresql://user:pass@localhost:port/db"
	WORKERS = 6
	# GAME_CHAT = (int|str)
	# chat/user id/username where you want to send the notification
	# can be group/channel/user
	# for channel and group you need to make the bot admin on that group
	GAME_CHAT = -1001234
	TZ = "Asia/Jakarta" # your local timezone
	INTERVAL = 30*60 # Interval for scanning new free games (in seconds)

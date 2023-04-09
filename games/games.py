from games import API_ID, API_HASH, BOT_SESSION, INTERVAL, WORKERS
from games.utils.epicgames import get_free_epic_games
from games.utils.gog import get_free_gog_games
from games.utils.steam import get_free_steam_games
from apscheduler import RunState
from apscheduler.schedulers.async_ import AsyncScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pyrogram import Client

class Games(Client):
	def __init__(self):
		name = self.__class__.__name__.lower()
		super().__init__(
			name,
			session_string=BOT_SESSION,
			api_id=API_ID,
			api_hash= API_HASH,
			workers=WORKERS,
			sleep_threshold=180
		)

	async def start_scheduler(self):
		self.scheduler = AsyncScheduler()
		await self.scheduler.__aenter__()
		if self.scheduler.state == RunState.stopped:
			await self.scheduler.add_schedule(self.epicgames, IntervalTrigger(seconds=INTERVAL))
			await self.scheduler.add_schedule(self.gog, IntervalTrigger(seconds=INTERVAL))
			await self.scheduler.add_schedule(self.steam, IntervalTrigger(seconds=INTERVAL))
			await self.scheduler.start_in_background()

	async def epicgames(self):
		await get_free_epic_games(self)

	async def gog(self):
		await get_free_gog_games(self)

	async def steam(self):
		await get_free_steam_games(self)

	async def start(self):
		await super().start()
		await self.start_scheduler()
		print("---[Free Games Notifier Services is Running...]---")

	async def stop(self, *args):
		await super().stop()
		print("---[Bye]---")
		print("---[Thankyou for using my bot...]---")

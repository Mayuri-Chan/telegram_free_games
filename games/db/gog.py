import threading

from games import BASE, SESSION
from sqlalchemy import Column, UnicodeText

class Gog(BASE):
	__tablename__ = "gog_list"
	name = Column(UnicodeText, primary_key=True)

	def __init__(self,name):
		self.name = name


	def __repr__(self):
		return "<Gog for %s>" % (self.name)


Gog.__table__.create(checkfirst=True)
GOG_INSERTION_LOCK = threading.RLock()

def add(name):
	with GOG_INSERTION_LOCK:
		prev = SESSION.query(Gog).get(name)
		if prev:
			SESSION.delete(prev)
			SESSION.commit()

		gog_filt = Gog(name)
		SESSION.merge(gog_filt)
		SESSION.commit()

def check_gog(name):
	with GOG_INSERTION_LOCK:
		find = SESSION.query(Gog).get(name)
		if find:
			return True
		return False

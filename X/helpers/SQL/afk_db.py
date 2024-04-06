from sqlalchemy import Boolean, Column, String, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Assuming these are defined elsewhere
from X.helpers.SQL import SESSION

Owner = 0

# Creating base
BASE = declarative_base()

class AfkDb(BASE):
    __tablename__ = "afk"
    user_id = Column(String(14), primary_key=True)
    is_afk = Column(Boolean, default=False)
    reason = Column(UnicodeText, default="")

    def __init__(self, user_id, is_afk=False, reason=""):
        self.user_id = str(user_id)
        self.is_afk = is_afk
        self.reason = reason

    def __repr__(self):
        return f"<AfkDb user_id={self.user_id}, is_afk={self.is_afk}, reason={self.reason}>"

class AfkManager:
    def __init__(self, session):
        self.session = session

    def set_afk(self, user_id, afk, reason=""):
        afk_entry = self.session.query(AfkDb).get(str(user_id))
        if afk_entry:
            self.session.delete(afk_entry)
        afk_db = AfkDb(user_id, afk, reason)
        self.session.add(afk_db)
        self.session.commit()

    def get_afk(self, user_id):
        afk_entry = self.session.query(AfkDb).get(str(user_id))
        if afk_entry:
            return {"afk": afk_entry.is_afk, "reason": afk_entry.reason}
        return None

    def load_afk(self):
        try:
            qall = self.session.query(AfkDb).all()
            return {int(entry.user_id): {"afk": entry.is_afk, "reason": entry.reason} for entry in qall}
        except Exception as e:
            print(f"Error loading AFK entries: {e}")
            return {}

    def close_session(self):
        self.session.close()

# Creating database tables
BASE.metadata.create_all(SESSION.bind)

# Creating instance of AfkManager
afk_manager = AfkManager(SESSION)

# Loading AFK entries
MY_AFK = afk_manager.load_afk()

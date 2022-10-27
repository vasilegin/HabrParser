from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from utils.files import get_assets

config = get_assets('config')
DATABASE_URI = config['url']['database']

engine = create_engine(DATABASE_URI)
session_factory = sessionmaker(bind=engine, autoflush=False)
Session = scoped_session(session_factory)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.files import get_assets

config = get_assets('config')
DATABASE_URI = config['url']['database']

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
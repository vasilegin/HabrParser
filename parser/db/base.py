from databases import Database
from sqlalchemy import create_engine, MetaData
from utils.files import get_assets

config = get_assets('config')
DATABASE_URL = config['url']['database']

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)
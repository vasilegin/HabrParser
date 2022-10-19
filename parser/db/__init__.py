from .articles import articles
from .comments import comments
from .base import metadata, engine

metadata.create_all(bind=engine)
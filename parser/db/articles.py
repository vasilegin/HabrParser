import sqlalchemy
from parser.db.base import metadata
import datetime

jobs = sqlalchemy.Table(
    "articles", 
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("timePublished", sqlalchemy.DateTime),
    sqlalchemy.Column("lang", sqlalchemy.String),
    sqlalchemy.Column("titleHtml", sqlalchemy.TEXT),
    sqlalchemy.Column("textHtml", sqlalchemy.TEXT),
    sqlalchemy.Column("postLabels", sqlalchemy.String),
    sqlalchemy.Column("author_fullname", sqlalchemy.String),
    sqlalchemy.Column("author_rating", sqlalchemy.String),
    sqlalchemy.Column("readingCount", sqlalchemy.Integer),
    sqlalchemy.Column("tags", sqlalchemy.Text),
    sqlalchemy.Column("classes", sqlalchemy.Text),
)
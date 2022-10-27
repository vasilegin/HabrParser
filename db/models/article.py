from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True)
    timePublished = Column(DateTime)
    lang = Column(String)
    titleHtml = Column(String)
    textHtml = Column(String)
    postLabels = Column(String)
    author_fullname = Column(String)
    author_rating = Column(String)
    readingCount = Column(Integer)
    tags = Column(String)
    classes = Column(String)

    def __init__(self, id, tP, lang, titleHtml, textHtml, pL, af, ar, rC, tags, classes ):
        self.id = id
        self.timePublished = tP
        self.lang = lang
        self.titleHtml = titleHtml
        self.textHtml = textHtml
        self.postLabels = pL
        self.author_fullname = af
        self.author_rating = ar
        self.readingCount = rC
        self.tags = tags
        self.classes = classes

    def __repr__(self):
        return "<Article(title='{}', author='{}', published={})>"\
                .format(self.titleHtml, self.author_fullname, self.timePublished)
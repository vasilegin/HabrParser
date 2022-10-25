from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Articles(Base):
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
    
    def __repr__(self):
        return "<Articles(title='{}', author='{}', published={})>"\
                .format(self.titleHtml, self.author_fullname, self.timePublished)
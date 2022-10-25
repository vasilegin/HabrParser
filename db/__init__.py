from .models import *
from .base import engine

Base.metadata.create_all(engine)
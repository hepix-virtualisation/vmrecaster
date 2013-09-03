from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import mapper

from sqlalchemy import ForeignKey

from sqlalchemy.orm import backref
try:
    from sqlalchemy.orm import relationship
except:
    from sqlalchemy.orm import relation as relationship


from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

from sqlalchemy.schema import UniqueConstraint


##########################################
# makes key value tables to increase flexibility.

Base = declarative_base()


class ImageUuidMapping(Base):
    __tablename__ = 'mapping'
    id = Column(Integer, primary_key=True)
    imageUuidSrc = Column(String(100),nullable = False)
    imageUuidDest = Column(String(100),nullable = False,unique=True)
    imagelistUuidDest = Column(String(100))
    def __init__(self, *args, **kwargs):
        self.imageUuidSrc = kwargs.get('imageUuidSrc', None)
        self.imageUuidDest = kwargs.get('imageUuidDest', None)
        self.imagelistUuidDest = kwargs.get('imagelistUuidDest', None)
        
    def __repr__(self):
        return "<ImageUuidMapping('%s','%s','%s')>" % (self.imageUuidDest,self.imageUuidSrc,self.imagelistUuidDest)


class Session(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(100),nullable = False,unique=True)
    created = Column(DateTime,nullable = False)
    def __init__(self,*args, **kwargs):
        self.uuid = kwargs.get('uuid', None)
        self.created = kwargs.get('created', None)
    def __repr__(self):
        return "<Session('%s','%s')>" % (self.uuid,self.created)
    

class EventType(Base):
    __tablename__ = 'event_type'
    id = Column(Integer, primary_key=True)
    name = Column(String(100),nullable = False,unique=True)
    def __init__(self,*args, **kwargs):
        self.name = kwargs.get('name', None)
    def __repr__(self):
        return "<EventType('%s')>" % (self.name)


class ImageEvent(Base):
    __tablename__ = 'image_event'
    id = Column(Integer, primary_key=True)
    fkSession = Column(Integer, ForeignKey(Session.id, onupdate="CASCADE", ondelete="CASCADE"),nullable = False)
    fkImageUuidMapping = Column(Integer, ForeignKey(ImageUuidMapping.id, onupdate="CASCADE", ondelete="CASCADE"),nullable = False)
    fkType = Column(Integer, ForeignKey(EventType.id, onupdate="CASCADE", ondelete="CASCADE"),nullable = False)
    created = Column(DateTime,nullable = False)
    def __init__(self,*args, **kwargs):
        self.fkSession = kwargs.get('fkSession', None)
        self.fkImageUuidMapping = kwargs.get('fkImageUuidMapping', None)
        self.fkType = kwargs.get('fkType', None)
        self.created = kwargs.get('created', None)
    def __repr__(self):
        return "<ImageEvent('%s','%s','%s','%s')>" % (self.fkSession, self.fkImageUuidMapping, self.fkType,self.created)




def init(engine):
    Base.metadata.create_all(engine)

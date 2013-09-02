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
    


class ImageEvent(Base):
    __tablename__ = 'image_event'
    id = Column(Integer, primary_key=True)
    fkSession = Column(Integer, ForeignKey(Session.id, onupdate="CASCADE", ondelete="CASCADE"))
    fkImageUuidMapping = Column(Integer, ForeignKey(ImageUuidMapping.id, onupdate="CASCADE", ondelete="CASCADE"))
    created = Column(DateTime,nullable = False)
    def __init__(self,imagelist,key,value):
        self.fkEndorser = imagelist
        self.key = key
        self.value = value
    def __repr__(self):
        return "<ImageEvent('%s','%s', '%s')>" % (self.fkEndorser, self.key, self.value)




def init(engine):
    Base.metadata.create_all(engine)

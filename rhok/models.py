from sqlalchemy import (
    Column,
    Integer,
    Text,
    Date,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value

class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    data = Column(Text)
    result = Column(Text)

    def __init__(self, date, data, result):
        self.date = date
        self.data = data
        self.result = result


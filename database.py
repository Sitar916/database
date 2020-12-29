import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship ,sessionmaker


DATABASE = 'postgres+psycopg2://postgres:@localhost:1572/Database'
engine = create_engine(DATABASE)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Competition(Base):
    __tablename__ = 'competition'
    num_partcipants = Column(Integer,primary_key = True)
    prize_fund = Column(Integer)
    def __init__(self,num_partcipants,prize_fund):
        self.num = num
        self.num_partcipants=num_partcipants
        self.prize_fund = prize_fund

class Game(Base):
    __tablename__ = 'game'
    game_name = Column(String,primary_key = True)
    game_jenre = Column(String)
    def __init__(self,game_name,game_jenre):
        self.game_jenre=game_jenre
        self.game_name = game_name

class GameName(Base):
    __tablename__ = 'game_name'
    online = Column(Integer,primary_key = True)
    max_online = Column(Integer)
    def __init__(self,online,max_online):
        self.max_online=max_online
        self.max=max

class Player(Base):
    __tablename__ = 'player'
    name = Column(String,primary_key = True)
    status_pc = Column(String)
    def __init__(self,name,status_pc):
        self.name =name
        self.status_pc = status_pc
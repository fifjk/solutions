from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import String, Integer, Boolean, Float

Base = declarative_base()

class Men(Base):
    __tablename__ = "men"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    alias = Column(String)
    media = Column(String)
    human = Column(Boolean)
    concern = Column(Integer or Float)

    def __repr__(self):
        return f"Men: {self.id}, {self.name}, {self.alias}, {self.media}, {self.human}, {self.concern}"

    def convert_to_tuple(self):
        return self.id, self.name, self.alias, self.media, self.human, self.concern

    def valid(self):
        return self.concern != -1

    @staticmethod
    def convert_from_tuple(tuple_):
        men = Men(id=tuple_[0], name=tuple_[1], alias=tuple_[2], media=tuple_[3], human=tuple_[4], concern=tuple_[5])
        return men


class Women(Base):
    __tablename__ = "women"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    alias = Column(String)
    media = Column(String)
    human = Column(Boolean)
    concern = Column(Integer or Float)

    def __repr__(self):
        return f"women: {self.id}, {self.name}, {self.alias}, {self.media}, {self.human}, {self.concern}"

    def convert_to_tuple(self):
        return self.id, self.name, self.alias, self.media, self.human, self.concern

    def valid(self):
        return self.concern != -1

    @staticmethod
    def convert_from_tuple(tuple_):
        women = Women(id=tuple_[0], name=tuple_[1], alias=tuple_[2], media=tuple_[3], human=tuple_[4], concern=tuple_[5])
        return women


class Other(Base):
    __tablename__ = "other"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    alias = Column(String)
    media = Column(String)
    human = Column(Boolean)
    concern = Column(Integer or Float)

    def __repr__(self):
        return f"other: {self.id}, {self.name}, {self.alias}, {self.media}, {self.human}, {self.concern}"

    def convert_to_tuple(self):
        return self.id, self.name, self.alias, self.media, self.human, self.concern

    def valid(self):
        return self.concern != -1

    @staticmethod
    def convert_from_tuple(tuple_):
        other = Other(id=tuple_[0], name=tuple_[1], alias=tuple_[2], media=tuple_[3], human=tuple_[4], concern=tuple_[5])
        return other

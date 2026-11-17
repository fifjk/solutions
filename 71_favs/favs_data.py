from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import String, Integer, Boolean

Base = declarative_base()

class Masculine(Base):
    __tablename__ = "masculine"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    aka = Column(String)
    media = Column(String)
    human = Column(Boolean)

    def __repr__(self):
        return f"Masculine: {self.id}, {self.aka} {self.name}, {self.media}, {self.human}"

    def convert_to_tuple(self):
        return self.id, self.name, self.aka, self.media, self.human

    def valid(self):
        return self.media != "-1"

    @staticmethod
    def convert_from_tuple(tuple_):
        masculine = Masculine(id=tuple_[0], name=tuple_[1], aka=tuple_[2], media=tuple_[3], human=tuple_[4])
        return masculine


class Feminine(Base):
    __tablename__ = "feminine"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    aka = Column(String)
    media = Column(String)
    human = Column(Boolean)

    def __repr__(self):
        return f"feminine: {self.id}, {self.aka} {self.name}, {self.media}, {self.human}"

    def convert_to_tuple(self):
        return self.id, self.name, self.aka, self.media, self.human

    def valid(self):
        return self.media != "-1"

    @staticmethod
    def convert_from_tuple(tuple_):
        feminine = Feminine(id=tuple_[0], name=tuple_[1], aka=tuple_[2], media=tuple_[3], human=tuple_[4])
        return feminine


class Other(Base):
    __tablename__ = "other"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    aka = Column(String)
    media = Column(String)
    human = Column(Boolean)

    def __repr__(self):
        return f"other: {self.id}, {self.aka} {self.name}, {self.media}, {self.human}"

    def convert_to_tuple(self):
        return self.id, self.name, self.aka, self.media, self.human

    def valid(self):
        return self.media != "-1"

    @staticmethod
    def convert_from_tuple(tuple_):
        other = Other(id=tuple_[0], name=tuple_[1], aka=tuple_[2], media=tuple_[3], human=tuple_[4])
        return other

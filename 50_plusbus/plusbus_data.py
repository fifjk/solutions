from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Date
from dateutil import parser
from tkinter import messagebox

Base = declarative_base()

class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    contact = Column(String or Integer)

    def __repr__(self):
        return f"Clients: {self.id} {self.last_name}, {self.contact}"

    def convert_to_tuple(self):
        return self.id, self.last_name, self.contact

    def valid(self):
        try:
            value = int(self.contact)
        except ValueError:
            return False
        return value <= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        clients = Clients(id=tuple_[0], last_name=tuple_[1], contact=tuple_[2])
        return clients


class Trips(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True)
    route = Column(String)
    date = Column(Date)
    capacity = Column(Integer)

    def __repr__(self):
        return f"Trips: {self.id} {self.route}, {self.date}, {self.capacity}"

    def convert_to_tuple(self):
        return self.id, self.route, self.date, self.capacity

    def valid(self):
        try:
            value = int(self.capacity)
        except ValueError:
            return False
        return value <= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        trips = Trips(id=tuple_[0], route=tuple_[1], date=tuple_[2], capacity=tuple_[3])
        return trips


class Bookings(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=False)
    seats = Column(Integer)

    def __repr__(self):
        return f"Bookings: {self.id} {self.client_id}, {self.trip_id}, {self.seats}"

    def convert_to_tuple(self):
        return self.id, self.client_id, self.trip_id, self.seats

    def valid(self):
        try:
            value = int(self.seats)
        except ValueError:
            return False
        return value <= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        bookings = Bookings(id=tuple_[0], client_id=tuple_[1], trip_id=tuple_[2], seats=tuple_[3])
        return bookings


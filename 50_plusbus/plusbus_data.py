from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Date
from dateutil import parser
from tkinter import messagebox

Base = declarative_base()

class Clients(Base):
    __tablename__ = "clients"
    last_name = Column(String, primary_key=True)
    contact = Column(String or Integer)

    def __repr__(self):
        return f"Clients: {self.last_name}, {self.contact}"

    def convert_to_tuple(self):
        return self.last_name, self.contact

    def valid(self):
        try:
            value = int(self.contact)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        clients = Clients(last_name=tuple_[0], contact=tuple_[1])
        return clients


class Trips(Base):
    __tablename__ = "trips"
    bus_id = Column(Integer, primary_key=True)
    route = Column(String)
    date = Column(Date)
    capacity = Column(Integer)

    def __repr__(self):
        return f"Trips: {self.bus_id} {self.route}, {self.date}, {self.capacity}"

    def convert_to_tuple(self):
        return self.bus_id, self.route, self.date, self.capacity

    def valid(self):
        try:
            value = int(self.capacity)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        trips = Trips(bus_id=tuple_[0], route=tuple_[1], date=tuple_[2], capacity=tuple_[3])
        return trips


class Bookings(Base):
    __tablename__ = "bookings"
    client_id = Column(Integer, primary_key=True)
    trip_id = Column(Integer)
    seats = Column(Integer)

    def __repr__(self):
        return f"Bookings: {self.client_id}, {self.trip_id}, {self.seats}"

    def convert_to_tuple(self):
        return self.client_id, self.trip_id, self.seats

    def valid(self):
        try:
            value = int(self.trip_id)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        bookings = Bookings(client_id=tuple_[0], trip_id=tuple_[1], seats=tuple_[2])
        return bookings


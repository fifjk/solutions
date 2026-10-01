from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete

from datetime import date
from plusbus_data import Clients, Trips, Bookings, Base

Database = 'sqlite:///plusbus.db'


def create_test_data():
    with Session(engine) as session:
        session.query(Clients).delete()
        session.query(Trips).delete()
        session.query(Bookings).delete()

        new_items = []
        new_items.append(Clients(last_name="Hello Kitty", contact="hellokitty@gmail.com"))
        new_items.append(Clients(last_name="Michael Jackson", contact=48357184))

        date_1 = date(day=28, month=10, year=2007)
        date_2 = date(day=24, month=2, year=2025)
        date_3 = date(day=12, month=5, year=2021)

        new_items.append(Trips(route="Mainland - Neverland", date=date_1, capacity=40))
        new_items.append(Trips(route="Moss Grotto - Bellhart", date=date_2, capacity=6))
        new_items.append(Trips(route="Copenhagen - Delhi", date=date_3, capacity=50))

        new_items.append(Bookings(client_id=20112, trip_id=19367193, seats=5))
        new_items.append(Bookings(client_id=88167, trip_id=13391073, seats=1))
        new_items.append(Bookings(client_id=49920, trip_id=22109481, seats=2))

        session.add_all(new_items)
        session.commit()

engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

create_test_data()
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
        new_items.append(Clients(id=20112, last_name="Hello Kitty", contact="hellokitty@gmail.com"))
        new_items.append(Clients(id=88167, last_name="Michael Jackson", contact=48357184))

        date_1 = date(day=28, month=10, year=2007)
        date_2 = date(day=24, month=2, year=2025)

        new_items.append(Trips(id=19367193, route="Mainland - Neverland", date=date_1, capacity=40))
        new_items.append(Trips(id=13391073, route="Moss Grotto - Bellhart", date=date_2, capacity=6))

        new_items.append(Bookings(id=18281, client_id=20112, trip_id=19367193, seats=5))
        new_items.append(Bookings(id=19083, client_id=88167, trip_id=13391073, seats=1))

        session.add_all(new_items)
        session.commit()


def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


def get_record(classparam, record_id):
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


def create_record(record):
    with Session(engine) as session:
        record.id = None
        session.add(record)
        session.commit()


# region clients functions
def update_clients(clients):
    with Session(engine) as session:
        session.execute(update(Clients).where(Clients.id == clients.id).values(last_name=clients.last_name, contact=clients.contact))
        session.commit()


def delete_hard_clients(clients):
    with Session(engine) as session:
        session.execute(delete(Clients).where(Clients.id == clients.id))
        session.commit()

def delete_soft_clients(clients):
    with Session(engine) as session:
        session.execute(update(Clients).where(Clients.id == clients.id).values(last_name=clients.last_name, contact=-1))
        session.commit()

# endregion clients functions

# region trips functions

def update_trips(trips):
    with Session(engine) as session:
        session.execute(update(Trips).where(Trips.id == trips.id).values(route=trips.route, date=trips.date, capacity=trips.capacity))
        session.commit()


def delete_hard_trips(trips):
    with Session(engine) as session:
        session.execute(update(Trips).where(Trips.id == trips.id))
        session.commit()


def delete_soft_trips(trips):
    with Session(engine) as session:
        session.execute(update(Trips).where(Trips.id == trips.id).values(route=trips.route, date=trips.date, capacity=-1))
        session.commit()

# endregion trips functions

# region bookings functions

def update_bookings(bookings):
    with Session(engine) as session:
        session.execute(update(Bookings).where(Bookings.id == bookings.id).values(client_id=bookings.client_id, trip_id=bookings.trip_id, seats=bookings.seats))
        session.commit()


def delete_hard_bookings(bookings):
    with Session(engine) as session:
        session.execute(update(Bookings).where(Bookings.id == bookings.id))
        session.commit()


def delete_soft_bookings(bookings):
    with Session(engine) as session:
        session.execute(update(Bookings).where(Bookings.id == bookings.id).values(client_id=bookings.client_id, trip_id=bookings.trip_id, seats=-1))
        session.commit()

# endregion bookings functions


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

create_test_data()
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
from favs_data import Masculine, Feminine, Other, Base

Database = 'sqlite:///favs.db'

def create_test_data():
    with Session(engine) as session:
        session.query(Masculine).delete()
        session.query(Feminine).delete()
        session.query(Other).delete()

        new_items = []
        new_items.append(Masculine(id=101, name="Viktor", aka="", media="Arcane", human=True))
        new_items.append(Masculine(id=102, name="Steve", aka="", media="Stranger Things", human=True))
        new_items.append(Masculine(id=103, name="Ryuk", aka="", media="Death Note", human=False))
        new_items.append(Masculine(id=104, name="Daffy Duck", aka="", media="Looney Tunes", human=False))

        new_items.append(Feminine(id=201, name="Tina Russo", aka="", media="Looney Tunes", human=False))
        new_items.append(Feminine(id=202, name="Ella Lopez", aka="", media="Lucifer", human=True))
        new_items.append(Feminine(id=203, name="Jinx", aka="Powder", media="Arcane", human=True))

        new_items.append(Other(id=301, name="Skitty", aka="", media="Pokémon", human=False))
        new_items.append(Other(id=302, name="Delcatty", aka="", media="Pokémon", human=False))

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
        session.add(record)
        session.commit()


def delete_data():
    with Session(engine) as session:
        session.query(Masculine).delete()
        session.query(Feminine).delete()
        session.query(Other).delete()

        session.commit()

# region masculine functions
def update_masculine(masculine):
    with Session(engine) as session:
        session.execute(update(Masculine).where(Masculine.id == masculine.id).values(name=masculine.name, aka=masculine.aka, media=masculine.media, human=masculine.human))
        session.commit()

def delete_hard_masculine(masculine):
    with Session(engine) as session:
        session.execute(delete(Masculine).where(Masculine.id == masculine.id))
        session.commit()
# endregion masculine functions

# region feminine functions
def update_feminine(feminine):
    with Session(engine) as session:
        session.execute(update(Feminine).where(Feminine.id == feminine.id).values(name=feminine.name, aka=feminine.aka, media=feminine.media, human=feminine.human))
        session.commit()

def delete_hard_feminine(feminine):
    with Session(engine) as session:
        session.execute(delete(Feminine).where(Feminine.id == feminine.id))
        session.commit()
# endregion feminine functions

# region other functions
def update_other(other):
    with Session(engine) as session:
        session.execute(update(Other).where(Other.id == other.id).values(name=other.name, aka=other.aka, media=other.media, human=other.human))
        session.commit()

def delete_hard_other(other):
    with Session(engine) as session:
        session.execute(delete(Other).where(Other.id == other.id))
        session.commit()
# endregion other functions


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

create_test_data()

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
from hmo_data import Men, Women, Other, Base

Database = 'sqlite:///hmo.db'

def create_test_data():
    with Session(engine) as session:
        session.query(Men).delete()
        session.query(Women).delete()
        session.query(Other).delete()

        new_items = []
        new_items.append(Men(id=1, name="Smeech", media="Arcane", human="False", concern=7))
        new_items.append(Men(id=2, name="Billy Hargrove", media="Stranger Things", human=True, concern=2))
        new_items.append(Men(id=3, name="Ryuk", media="Death Note", human="False", concern=8))
        new_items.append(Men(id=4, name="Daffy Duck", media="Looney Tunes", human="False", concern=5))


# women: Tina Russo, Ella Lopez, Stella
# men: Smeech, Billy Hargrove, Ryuk, Daffy Duck(episode 22 "beauty school")
# other: 2 or 3-headed street lamp, ziplock bag

# missy: smeech = 8, billy = 3, ryuk = 4, daffy duck = 5, tina = 2, ella = 1, stella = 7, lamp = 10, ziplock = 9


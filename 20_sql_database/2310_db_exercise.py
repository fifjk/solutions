"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Anvend det, du har lært i dette kapitel om databaser, på en denne opgave.

Trin 1:
Opret en ny SQLite database "2311_my_second_sql_database.db" i din solutions mappe.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() for begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra 2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Det skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import create_engine, select


Database = 'sqlite:///2311_my_second_sql_database.db'
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Customer: id={self.id}, name={self.name}, address={self.address}, age={self.age}"

    def convert_to_tuple(self):
        return self.id, self.name, self.address, self.age

    def valid(self):
        try:
            value = int(self.age)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Person
        customer = Customer(id=tuple_[0], name=tuple_[1], address=tuple_[2], age=tuple_[3])
        return customer


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_number = Column(Integer)
    price = Column(Float)
    brand = Column(String)

    def __repr__(self):
        return f"Product: id={self.id}, product_number={self.product_number}, price={self.price}, brand={self.brand}"

    def convert_to_tuple(self):
        return self.id, self.product_number, self.price, self.brand

    def valid(self):
        try:
            value = int(self.product_number)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Person
        product = Product(id=tuple_[0], product_number=tuple_[1], price=tuple_[2], brand=tuple_[3])
        return product


def create_test_data():
    with Session(engine) as session:
        session.query(Customer).delete()
        session.query(Product).delete()

        customer_table = []
        customer_table.append(Customer(id=101, name="Peter", address="McDonald's Street", age=18))
        customer_table.append(Customer(id=102, name="Lauren", address="Pizza Street", age=21))
        customer_table.append(Customer(id=103, name="Casey", address="Pasta Street", age=15))

        product_table = []
        product_table.append(Product(id=101, product_number=39102, price=2.99, brand="7-Eleven"))
        product_table.append(Product(id=102, product_number=23810, price=4.99, brand="Zara"))
        product_table.append(Product(id=103, product_number=94712, price=8.49, brand="H&M"))

        session.add_all(customer_table)
        session.add_all(product_table)
        session.commit()


def select_all(classparam):  # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

create_test_data()

print(get_record(Customer, 101))
print(get_record(Product, 102))

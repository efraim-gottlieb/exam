import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons (
        person_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT UNIQUE NOT NULL)
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        color TEXT NOT NULL,
        owner_id INTEGER,
        FOREIGN KEY (owner_id) REFERENCES persons(person_id))
        """)

    def insert_person(self, person :object):
        self.cursor.execute("""
        INSERT INTO persons (person_id, name, age, email)
        VALUES """ + f"('{person.person_id}', '{person.name}', {person.age}, '{person.email}')")
        self.connection.commit()
    
    def insert_car(self, car :object):
        self.cursor.execute("""
        INSERT INTO cars (car_id, brand, model, year, color, owner_id)
        VALUES """ + f"('{car.car_id}', '{car.brand}', '{car.model}', {car.year}, '{car.color}', '{car.owner_id}')")
        self.connection.commit()

    def get_all_persons(self):
        persons = self.cursor.execute('SELECT * FROM persons')
        persons = persons.fetchall()
        return persons

    def get_all_cars(self):
        cars = self.cursor.execute('SELECT * FROM cars')
        cars = cars.fetchall()
        return cars

    def get_person_by_id(self, person_id):
        person = self.cursor.execute('SELECT * FROM persons WHERE person_id = ?',
        (person_id,))
        person = person.fetchone()
        if person:
            return person
        else:
            return False

    def get_cars_by_owner(self, owner_id):
        cars = self.cursor.execute('SELECT * FROM cars WHERE owner_id = ?',
        (owner_id,))
        cars = cars.fetchall()
        if cars:
            return cars
        else:
            return False

    def update_person(self, person):
        self.cursor.execute(
            "UPDATE persons SET name = ?, age = ?, email = ? WHERE person_id = ?",
            (person.name, person.age, person.email, person.person_id)
        )
        self.connection.commit()

    def delete_person(self, person_id):
        self.cursor.execute('DELETE FROM persons WHERE person_id = ?', (person_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()

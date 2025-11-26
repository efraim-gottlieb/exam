import sqlite3
from session import session
import io
import csv
from fastapi import HTTPException

class DatabaseManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_soldiers_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS soldiers (
        id INTEGER PRIMARY KEY,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        DistanceFromBase INT NOT NULL,
        PlacementStatus TEXT NOT NULL)
        """)
        self.connection.commit()

    def create_rooms_table(self):
       self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY,
        house_id INTEGER NOT NULL,
        house_name TEXT NOT NULL
        )
        """)
       self.connection.commit()


    def import_soldiers_csv(self, soldiers):

        # Read CSV content
        for row in soldiers:
            row = vars(row)
            self.cursor.execute("""
                    INSERT INTO soldiers (id, FirstName, LastName, Gender, DistanceFromBase, PlacementStatus)
                    VALUES (?, ?, ?, ?, ?)
                """, (row['id'],row['FirstName'],row['LastName'],row['DistanceFromBase'],row['PlacementStatus']))
        self.connection.commit()

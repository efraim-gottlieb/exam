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


    def import_soldiers_csv(self, csv_content: bytes):
      try:
          # Read CSV content
          csv_text = csv_content.decode('utf-8')
          csv_reader = csv.reader(io.StringIO(csv_text))
          
          added = 0
          not_added = 0
          # Append rows to soldiers table
          for row in csv_reader:
            print(row)
            if row[0][0] != '8':
              not_added += 1
              continue
              
            self.cursor.execute("""
                INSERT INTO soldiers (id, FirstName, LastName, Gender, DistanceFromBase, PlacementStatus)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (row[0],row[1],row[2],row[3],row[4],'waiting'))
            added += 1
          
          self.connection.commit()
  
          return {
              "message": f"Successfully imported {added} soldiers from CSV",
              "added": added,
              "not added": not_added
          }
      except Exception as e:
          self.connection.rollback()
          raise HTTPException(status_code=400, detail=f"Error importing CSV: {str(e)}")
      finally:
          self.connection.close()
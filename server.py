from fastapi import FastAPI, HTTPException, UploadFile, File
import csv
import io
from DBmanager import DatabaseManager
DB_PATH = 'data.sqlite'
DBmanager = DatabaseManager(DB_PATH)
app = FastAPI()
from soldier import Soldier
from dwelling_hoses import DwellingHose
from houses_managment import HouseManager
a = HouseManager()

@app.post("/assignWithCsv")
async def upload_csv(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV file")
    
    # Read file content
    csv_content = await file.read()
    # Import CSV and store in database
    reader = list(csv.reader(csv_content.decode('utf-8').splitlines()))[1:]
    soldiers = []
    for soldier in reader:
        if soldier[0][0] == '8' and "".join([n for n in soldier[0] if int(n) in [i for i in range(0,10)]]) == soldier[0]:
            soldiers.append(Soldier(soldier[0], soldier[1], soldier[2], soldier[3], soldier[4], int(soldier[5]), 'waiting'))
            
    result = a.soldier_deployment(soldiers)
    return result

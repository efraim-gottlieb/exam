from fastapi import FastAPI, HTTPException, UploadFile, File
import csv
from DBmanager import DatabaseManager
from soldier import Soldier
from houses_managment import HouseManager

DB_PATH = 'data.sqlite'
DBmanager = DatabaseManager(DB_PATH)
app = FastAPI()

HousesManager = HouseManager()

soldiers_list= []

@app.post("/assignWithCsv")
async def upload_csv(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV file")
    global soldiers_list 
    # Read file content
    csv_content = await file.read()
    # Import CSV and store in database
    reader = list(csv.reader(csv_content.decode('utf-8').splitlines()))[1:]
    soldiers = []
    for soldier in reader:
        if soldier[0][0] == '8' and "".join([n for n in soldier[0] if int(n) in [i for i in range(0,10)]]) == soldier[0]:
            soldiers.append(Soldier(soldier[0], soldier[1], soldier[2], soldier[3], soldier[4], int(soldier[5]), 'waiting'))

    result = HousesManager.soldier_deployment(soldiers)
    soldiers_list = soldiers
    return result

@app.get("/space")
def get_house_space():
    return HousesManager.get_houses_info()

@app.get("/space/{house_id}")
def get_house_space(house_id):
    try:
        if int(house_id) in HousesManager.get_houses_info():
            return HousesManager.get_houses_info()[int(house_id)]
        else:
            HTTPException(status_code=400, detail="house noy found")
    except:
        HTTPException(status_code=400, detail="enter curent id")

@app.get('/waitingList')
def get_waitingList():
    return {'Waiting List':[so for so in soldiers_list if so.PlacementStatus != 'assigned']}


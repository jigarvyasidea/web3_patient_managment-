from fastapi import FastAPI , Path , HTTPException, Query
import json

app = FastAPI()

# Load JSON data
def load_data():
    with open('patient.json', 'r') as f:
        return json.load(f)

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"}

@app.get("/view")
def view():
    return load_data()

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., Description="id of the patient in the DB", example="p001")):
    data = load_data()

    # Direct dictionary lookup
    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code = 404, detail='patientnot found')
 # agar is project me kuch galt hoga to we railse HTTPException 


 # Query Paramenter :- 
 # hum Query paramenter ko option bta sakte hai 

 # ? ke paad key : value hoti h 
 # ege /patients/city=Delhi&sort_by=age

 # Ab hum end point banayege to sort patient 
 # we sort on basic on weight , height and BMI 


# Query parameter is adiitonal parameter it user for mutipllex prpost like paggin, searching , sorting etc

# best part about Query paramenter in optional 

# ?the we will write Query parameter




@app.get("/sort")
def sort_patient(sort_by:str = Query(..., description='sort on the basis of height, weight and BMI'), order: str = Query('asc', description=" sort in assending and desending  order"))

# defult value set kar sakte h 
# meta data add kar sakte h 
# or metadata add kar sakte h 

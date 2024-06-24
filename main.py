from fastapi import FastAPI, HTTPException
import pandas as pd
import os

# Get the current file directory
current_dir = os.path.dirname(os.path.abspath(__file__))
dataset = os.path.join(current_dir,"model2020_department1.csv")

# Create the FastAPI app
app = FastAPI()

# Load dataset from CSV into a DataFrame and then into a dictionary
df = pd.read_csv(dataset)
students_data = pd.Series(df.Department.values, index=df['studentid']).to_dict()

@app.get("/department/{student_id}")
def get_department(studentid: int):
    department = students_data.get(studentid)
    if department is None:
        raise HTTPException(status_code=404, detail="studentid not found")
    return {"studentid": studentid, "Department": department}




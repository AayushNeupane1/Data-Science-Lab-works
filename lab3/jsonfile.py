# 4. Writing and Reading JSON Data
# ● Stores student details (ID, name, and marks) in a JSON file
# ● Reads the JSON file and displays the student information
# ● Handles exceptions related to file access and JSON decoding

import json

#student ko json data
students = [

    {"ID":1, "Name":"Aayush","Marks": 85},
    {"ID":2, "Name":"Aastha","Marks": 90},
    {"ID":3, "Name":"Jeevan","Marks": 78}
]
with open("qst4.json", "w") as f:
    json.dump(students,f)
print("Student details written in JSON file")
try:
    with open("qst4.json", "r") as f:
        data = json.load(f)
        print("Student Details:")
        for student in data:
            print(f"ID: {student['ID']}, Name:{student['Name']}, Marks:{student['Marks']}")
            
except FileNotFoundError:
    print("File not found.")
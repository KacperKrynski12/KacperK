
import json


dane = {}

with open("Nowy Dokument tekstowy.json", "r") as f:
    dane = json.load(f)

#GORZEJ
for x in dane["employees"]:
    pass

#LEPIEJ
for employee in dane["employees"]:
    employee_name = employee.get("name")
    print(employee_name)

dane = {
  "employees": [
    {
      "name": "John Doe",
      "age": 35,
      "department": "Marketing",
      "salary": 50000,
      "contact": {
        "email": "john.doe@company.com",
        "phone": "555-1234",
        "address": {
          "street": "456 Second St",
          "city": "Anytown",
          "state": "CA",
          "zip": "67890"
        }
      }
    },
    {
      "name": "Jane Smith",
      "age": 28,
      "department": "Sales",
      "salary": 40000,
      "status": "True",
      "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
      }
    },
    {
      "name": "Bob Johnson",
      "age": 42,
      "department": "Engineering",
      "salary": 60000,
      "status": "False",
      "project": {
        "name": "Project X",
        "start_date": "2022-01-01",
        "end_date": "2022-12-31"
      }
    }
  ]
}

# print(dane.keys())

# print(type(dane["employees"]))
# print(dane["employees"][0]["contact"]["email"])
# employees = dane["employees"][1]["name"]
# print(employees)
# employees=dane["employees"][3]["street"]
# print (employees)

# ulica1pracownika = dane["employees"][0]["contact"]["address"]["street"]
# print(ulica1pracownika)
# # print(dane["employees"][1]["address"]["street"])
#  print(dane["employees"][2]["project"]["name"])

# print(dane["employees"][1]["age"])
# print(dane["employees"][2]["department"])
# print (type(dane["employees"]))
# print(dane["employees"][1]["name"])
# print(dane["employees"][2]["project"]["end_date"])
# print(dane["employees"][0])
# print (type(dane["employees"]))
# ImionaPracownikow= Imie1pracownika, Imie2pracownika, Imie3pracownika
# print list(ImionaPracownikow)
# with open("kod.py", "r") as file:
    #do_stuff()
#     pass

# int_value = 12
# float_value = 12.12
# print(str(int_value))
# imionapracownikow2=[]
# print(dane["employees"])
# employee_list = dane["employees"]
# for employee in employee_list:
#     status = employee.get("status", "")
#     if status == "True":
#       employee_name = employee["name"]
#       employee_salary = employee["salary"]
#       employee_name_salary = (employee_name, employee_salary)
#       imionapracownikow2.append(employee_name_salary)
    # print("Name of employee: " + employee_name)
    # print(f"Name of employee: {int_value}")
#     print("Name of employee: %s" % int_value)
# lista2 = [(employee["name"],employee["salary"]) for employee in dane["employees"] if employee.get("statHus", "") == "True"]
  

#     imionapracownikow2.append(employee_name)
# print(lista2)

# imiona_pracownikow3 = [employee["name"] for employee in dane["employees"] if employee["salary"] > 50000]
# # Imie1pracownika = dane["employees"][0]["name"]
# # Imie2pracownika = dane["employees"][1]["name"]
# # Imie3pracownika = dane["employees"][2]["name"]
# # ImionaPracowników=[Imie1pracownika, Imie2pracownika, Imie3pracownika]

# # for y in ImionaPracowników:
# #     print(y)

# # for iterator in collection:
# # do_stuff()

# Lista, set, tuple, dict
# tuple = (dane, dane)

# tuple[0] = imionapracownikow2

# bool_value = True

# if len(imionapracownikow2) > 0:
#     #do_stuff()
#     pass
# elif len(imionapracownikow2) == 0:
#     print("Nie mam pracownikow")
# else:
#     print("lista z negatywnym indexem")
# import json

# file_path= "Nowy Dokument tekstowy.json"
# with open("Nowy Dokument tekstowy.json", "r") as file:
#     dane = json.load(file)

# Imię1pracownika = dane["employees"][0]["name"]
# print(Imię1pracownika)

# zmienna = "37 lat"
# for employee in (dane["employees"]):
#    name = employee.get('name')
#    age = employee.get('age')
#    salary = employee.get('salary')
#    department = employee.get('department')
#    print(f"Name : {name}, Age: {age}, Salary:{salary}, Department:{department}")
   




  
          
  

# imie = (dane["employees"][0]["name"])

# if imie =="John Doe2":
#     print("Pan pierwszy w tabelce ma na imię John Doe")
# elif imie =="John Doe":
#     print("Luzik arbuzik")
# else:
#     print("Nie ma takiego człowieka")

   
# wiek1pracownika = dane["employees"][0]["age"]

# while wiek1pracownika < 50:
#     print("Pracownik ma lat mniej niż 50")
#     wiek1pracownika = wiek1pracownika + 2
#     if wiek1pracownika == 50:
#         break

# for xd in "Bartek":
#     print(xd)
  
# for aha in range(2,10,2):
#     print (aha)

# if (dane)["employees"][0]["name"] == "John Doe":
#     print("tak")

# Pensja = (dane["employees"][0]["salary"])
# while Pensja != 60000:
#       print(Pensja)
#       Pensja = Pensja + 2000


# pracownicy = (dane["employees"])

# for pracownicyy in pracownicy:
#     name = pracownicyy.get("name")
#     age = pracownicyy.get("age")
#     status = pracownicyy.get("status")
#     print(f"Name : {name}, Age : {age}, status : {status}")
# employees = dane["employees"]
# def funkcja():
#     for employee in employees:
#         if employees["name"].split()[-1].lower() = last_name.lower():

# def sumadlasalary('employees'):
#     return sum(employee["salary"] for employee in employees)
   
# suma wszystkich = sumarydlasalary(dane["employees"])
# print(f"Suma wynagrodzeń dla wszystkich pracowników :{suma wszystkich}")

for i in dane["employees"]:
    name = i.get("name")
    age = i.get("age")
    print(f"Name: {name} , Age: {age}")
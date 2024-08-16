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

# class Employee:
#    def __init__(self, name, age, department, salary,):
#        self.name = name
#        self.age = age
#        self.department = department
#        self.salary = salary
# def average_salary(employees: list[Employee]) -> float:
#    total_salary = sum(employee.salary for employee in employees)
#    return total_salary / len(employees)
# # Tworzenie obiektów Employee z danych
# employees = []
# for emp_data in dane["employees"]:
#    # Wydzielanie podstawowych danych
#    age = emp_data["age"]
#    department = emp_data["department"]
#    salary = emp_data["salary"]
#    # Tworzenie obiektu Employee
#    employee = Employee(emp_data["name"], age, department, salary)
#    employees.append(employee)
# # Obliczanie średniej pensji
# avg_salary = average_salary(employees)
# print(f"Średnia pensja pracowników: {avg_salary}")


# class Employee:
#    def __init__(self, name, age, department, salary,):
#        self.name = name
#        self.age = age
#        self.department = department
#        self.salary = salary

# def podajdanepracownika(self):
#        return f"{self.name}, {self.age}, {self.department}, {self.salary}"
# dane = Employee("Janek", 25, "brak", 15000)
# print(employee.podajdanepracownika)

    
  

  

# class contact(Employee):
#     def __init__(self, name, age, department, salary):
#         super().__init__(name, age, department, salary)
#         self.contact = contact

#     def podajwiek(self):
#         return self.age.get("age")
    
# class project2(Employee):
#     def __init__(self, name, age, department, salary, project):
#         super().__init__(name, age, department, salary)
#         self.project = project
#     def Podajprojekt(self):
#         return self.nazwaprojektu.get("project")
class Employee:
   def __init__(self, name, age, department, salary):
       self.name = name
       self.age = age
       self.department = department
       self.salary = salary
   def __str__(self):
       return f"{self.name}, {self.department}, {self.salary}"
   
class PracownikzPolemContact(Employee):
       def __init__(self,name,age,department,salary,contact):
           super().__init__(name,age,department,salary)
           self.contact = contact
       def pokazywaniecontactu(self):
           print(f"numer telefonu to {self.contact['phone']}")

class pracownikzpolemproject(Employee):
    def __init__(self, name, age, department, salary, project):
        super().__init__(name, age, department, salary)
        self.project = project
    
    def display_project_details(self):
       print(f"Project Details for {self.name}:")
       print(f"Project Name: {self.project['name']}")
       print(f"Start Date: {self.project['start_date']}")
       print(f"End Date: {self.project['end_date']}")

class PracownikZeStatusem(Employee):
   def __init__(self, name, age, department, salary, status):
       super().__init__(name, age, department, salary)
       self.status = status
   def display_status(self):
       status_str = "Active" if self.status == "True" else "Inactive"
       print(f"Status for {self.name}: {status_str}")

employees = []
for dane2 in dane["employees"]:
   name = dane2["name"]
   age = dane2["age"]
   department = dane2["department"]
   salary = dane2["salary"]
   if "contact" in dane2:
       employee = PracownikzPolemContact(name, age, department, salary, dane2["contact"])
   elif "project" in dane2:
       employee = pracownikzpolemproject(name, age, department, salary, dane2["project"])
   elif "status" in dane2:
       employee = PracownikZeStatusem(name, age, department, salary, dane2["status"])
   else:
       employee = Employee(name, age, department, salary)
   employees.append(employee)

def process_employee(employee):
   if isinstance(employee, PracownikzPolemContact):
       employee.pokazywaniecontactu()
   elif isinstance(employee, pracownikzpolemproject):
       employee.display_project_details()
   elif isinstance(employee, PracownikZeStatusem):
       employee.display_status()
   else:
       print(f"{employee.name}")


# Wywołanie funkcji dla każdego pracownika
for employee in employees:
   process_employee(employee)
 

       
       
  


  
    
  
        
      

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
zmienna = (dane["employees"][1])
x = zmienna.values()
print(zmienna.get("name"))




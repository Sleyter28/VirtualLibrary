class Employee:
    id = ""
    employee_id = ""
    name = ""
    last_name = ""
    middle_name = ""
    position = ""

    def __init__(self, id, employee_id, name, last_name, middle_name, position):
        self.id = id
        self.employee_id = employee_id
        self.name = name
        self.last_name = last_name
        self.middle_name = middle_name
        self.position = position
        print("Employee created successfully")


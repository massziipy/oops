class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return self.name +" earns Rs" + str(self.salary) + " per year"


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

    def display_info(self):
        return Employee.display_info(self) + " and manages the " + self.department + " department"


class CEO(Manager):
    def __init__(self, name, salary, department, company):
        Manager.__init__(self, name, salary, department)
        self.company = company

    def display_info(self):
        return Manager.display_info(self) + " at " + self.company


employee1 = Employee("Rishan    ", 50000)
manager1 = Manager("Falah", 80000, "Marketing")
ceo1 = CEO("Fidha", 200000, "Executive", "Baabte")

print(employee1.display_info())
print(manager1.display_info())
print(ceo1.display_info())

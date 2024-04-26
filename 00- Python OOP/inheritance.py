class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary


class Developer(Employee):
    def __init__(self, x, y, a):
        super().__init__(x, y)
        
        self.programming_language = a

    def write_code(self):
        return f"{self.name} is writing code in {self.programming_language}."



class Manager(Employee):
    def __init__(self, name, salary, d):
        super().__init__(name, salary)
        self.department = d

    def manage_team(self):
        return f"{self.name} is managing the {self.department} team."

# Example usage
developer = Developer("Alice", 60000, "Python")
print(developer.write_code())
print("Salary:", developer.calculate_pay())

manager = Manager("Bob", 80000, "Engineering")
print(manager.manage_team())
print("Salary:", manager.calculate_pay())


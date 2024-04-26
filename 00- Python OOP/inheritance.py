class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary


class Developer(Employee):
    def __init__(self, name, salary, progLang):
        super().__init__(name, salary)
        
        self.programming_language = progLang

    def write_code(self):
        return f"{self.name} is writing code in {self.programming_language}."



class Manager(Employee):
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.department = dept

    def manage_team(self):
        return f"{self.name} is managing the {self.department} team."

# Example usage
developer = Developer("Alice", 60000, "Python")
print(developer.write_code())
print("Salary:", developer.calculate_pay())

manager = Manager("Bob", 80000, "Engineering")
print(manager.manage_team())
print("Salary:", manager.calculate_pay())


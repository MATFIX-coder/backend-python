from abc import *

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def calculate_salary(self):
        return self.salary + self.team_size * 5000

class Developer(Employee):
    def __init__(self, name, salary, projects):
        super().__init__(name, salary)
        self.projects = projects

    def calculate_salary(self):
        return self.salary + self.projects * 3000

manager = Manager("Пашка", 1500, 3)
print(manager.calculate_salary())
developer = Developer("Гоша", 2000, 5)
print(developer.calculate_salary())
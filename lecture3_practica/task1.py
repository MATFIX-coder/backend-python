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
        self.name = name
        self.salary = salary
        self.team_size = team_size

    def calculate_salary(self):
        return self.salary + self.team_size * 5000

class Developer(Employee):
    def __init__(self, name, salary, projects):
        self.name = name
        self.salary = salary
        self.projects = projects

    def calculate_salary(self):
        return self.salary + self.projects * 3000
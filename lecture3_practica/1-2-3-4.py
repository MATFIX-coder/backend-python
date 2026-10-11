from datetime import *
from abc import *

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Книга: {self.title}, автор: {self.author} была издана {self.year}"

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author

    @property
    def age(self):
        return datetime.today().year - self.year

    @age.setter
    def age(self, age):
        self.year = datetime.today().year - age

    @classmethod
    def from_string(cls, string):
        title, author, year = string.split(";")
        return cls(title, author, int(year))

    def print_info(self):
        print(self.info())

class Ebook(Book):
    def __init__(self, title, author, year, format):
        self.title = title
        self.author = author
        self.year = year
        self.format = format

    def info(self):
        return f"Книга: {self.title}, автор: {self.author} была издана {self.year} в формате {self.format}"

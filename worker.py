from dataclasses import dataclass


@dataclass
class Worker:
    name: str
    surname: str
    position: str = None
    salary_per_hour: float = 18
    worked_in_hour = 0
    company: str = None
    age: int = 0
    sex: str = None
    phone_number: str = None
    email: str = None
    salary: float = 0

    def __repr__(self):
        return f"*     Name: {self.name}, Surname: {self.surname},\n      Position: {self.position}, Salary: {self.salary}\n "

    def count_salary(self):
        self.salary = self.salary_per_hour * self.worked_in_hour

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
        return f"   *     Name: {self.name}, Surname: {self.surname},\n" \
               f"         Position: {self.position}, Salary: {self.salary}\n "

    def show_contact(self):
        return f"   *     Name: {self.name}, Surname: {self.surname},\n" \
               f"         Phone number: {self.phone_number}, email: {self.email}\n"

    def show_finance(self):
        return f"   *     Name: {self.name}, Surname: {self.surname},\n" \
               f"         Salary: {self.salary}$, = {self.salary_per_hour}$ X {self.worked_in_hour}h\n"

    def count_salary(self):
        self.salary = self.salary_per_hour * self.worked_in_hour

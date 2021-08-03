from dataclasses import dataclass

@dataclass
class Worker:
    name: str
    surname: str
    position: str = None
    salary_per_hour: float = 18
    worked_in_hour: int = 0
    company: object = None
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

    def show_workers_to(self):
        return f"   *     Name: {self.name}, Surname: {self.surname},\n               Position: {self.position}\n"

    def count_salary(self):
        print(self.salary, self.worked_in_hour)
        self.salary = self.salary_per_hour * self.worked_in_hour

    def set_salary_for_worker(self, value):
        self.salary = value

    def set_phone_for_worker(self, phone_number):
        self.phone_number = phone_number

    def set_email_for_worker(self, email):
        self.email = email

    def set_position_for_worker(self, position):
        self.position = position
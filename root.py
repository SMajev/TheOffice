from dataclasses import dataclass
from worker import Worker
import pickle


class TheOffice:
    def __init__(self, company_name):
        self.company_name = company_name
        self.all_of_them = self.load_workers_from_file()

    def __repr__(self):
        return f"Company: {self.company_name},\nWorkers:\n{self.all_of_them}"

    def add_worker(self, name, surname, sallary, age=None, sex=None, phone_number=None, email=None):
        unit = Worker(name, surname, sallary, self, age, sex, phone_number, email)
        self.all_of_them.append(unit)

    def show_workers(self):
        for worker in self.all_of_them:
            print(worker)

    def set_salary_for_worker(self, worker_name, worker_surname, value):
        for worker in self.all_of_them:
            if worker.name == worker_name:
                if worker.surname == worker_surname:
                    worker.salary_per_hour = value

    def set_phone_for_worker(self, worker_name, worker_surname, phone_number):
        for worker in self.all_of_them:
            if worker.name == worker_name:
                if worker.surname == worker_surname:
                    worker.phone_number = phone_number

    def set_email_for_worker(self, worker_name, worker_surname, email):
        for worker in self.all_of_them:
            if worker.name == worker_name:
                if worker.surname == worker_surname:
                    worker.email = email

    def set_position_for_worker(self, worker_name, worker_surname, position):
        for worker in self.all_of_them:
            if worker.name == worker_name:
                if worker.surname == worker_surname:
                    worker.position = position

    def show_contact_worker(self, worker_name, worker_surname):
        for worker in self.all_of_them:
            if worker.name == worker_name:
                if worker.surname == worker_surname:
                    worker_contact_string = f"*     Name: {worker_name}, Surname: {worker_surname},\n" \
                                            f"      Phone number: {worker.phone_number}, email: {worker.email}\n"
                    return worker_contact_string

    def add_hour_worker(self, worker_name, worker_surname, hours):
        for worker in self.all_of_them:
            if worker.name == worker_name:
                if worker.surname == worker_surname:
                    worker.worked_in_hour += hours

    def rem_hour_worker(self, worker_name, worker_surname, hours):
        for worker in self.all_of_them:
            if worker.name == worker_name:
                if worker.surname == worker_surname:
                    worker.worked_in_hour -= hours

    def count_salary_for_everyone(self):
        for worker in self.all_of_them:
            worker.count_salary()

    def safe_workers_to_file(self):
        with open("workers.pickle", "wb") as out_file:
            pickle.dump(self.all_of_them, out_file)

    def load_workers_from_file(self):
        with open("workers.pickle", "rb") as in_file:
            workers = pickle.load(in_file)
            return workers


my_office = TheOffice("MROK")

my_office.count_salary_for_everyone()

my_office.safe_workers_to_file()

print("\n\n")

my_office.show_workers()

print("\n\n")

print(my_office.show_contact_worker("Szymon", "Majewski"))
print(my_office.show_contact_worker("Kuba", "Andrzejuk"))
print(my_office.show_contact_worker("Ludwika", "Arseniuk"))
print(my_office.show_contact_worker("Przemek", "Puchalski"))

print("\n\n\n\n")

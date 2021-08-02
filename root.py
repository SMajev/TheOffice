from worker import Worker
import pickle
import datetime
from timelog import TimeLog


class TheOffice:
    def __init__(self, company_name):
        self.company_name = company_name
        self.all_of_them = self.load_workers_from_file()
        self.all_of_logs = self.load_logs_from_file()
        self.count_salary_for_everyone()
        self.sort_workers_by_surname()
        self.now = datetime.datetime.now().strftime('\nDate: %d, %b %Y, Time: %H:%M:%S\n')

        self.safe_logs_to_file()
        print(self.now)

    def __repr__(self):
        return f"Company: {self.company_name},\n"  # Workers:\n{self.all_of_them}"

    def add_worker(self, name, surname, sallary=0, age=None, sex=None, phone_number=None, email=None):
        unit = Worker(name, surname, sallary, self, age, sex, phone_number, email)
        self.all_of_them.append(unit)
        self.add_log("add worker")

    def add_log(self, operation):
        print("List of Logs:\n")
        log = TimeLog(operation)
        self.all_of_logs.append(log)

    def sort_workers_by_surname(self):
        self.all_of_them.sort(key=lambda x: x.surname)

    def sort_workers_by_name(self):
        self.all_of_them.sort(key=lambda x: x.name)

    def sort_workers_by_position(self):
        self.all_of_them.sort(key=lambda x: x.position)

    def show_workers(self):
        self.add_log("Worker list")
        print(f"Time: {self.clock_working()}")
        for worker in self.all_of_them:
            print(worker)

    def show_logs(self):
        for log in self.all_of_logs:
            print(log)

    def show_contact_worker(self, worker_name, worker_surname):
        self.clock_working()
        for worker in self.all_of_them:
            if worker.name == worker_name:
                if worker.surname == worker_surname:
                    print(worker.show_contact())

    def show_contact_all_of_them(self):
        for worker in self.all_of_them:
            print(worker.show_contact())

    def show_finance(self):
        for worker in self.all_of_them:
            print(worker.show_finance())

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
        with open(".workers.pickle", "wb") as out_file:
            pickle.dump(self.all_of_them, out_file)

    def load_workers_from_file(self):
        with open(".workers.pickle", "rb") as in_file:
            workers = pickle.load(in_file)
            return workers

    def safe_logs_to_file(self):
        with open(".logs.pickle", "wb") as out_files:
            pickle.dump(self.all_of_logs, out_files)

    def load_logs_from_file(self):
        with open(".logs.pickle", "rb") as in_files:
            logs = pickle.load(in_files)
            return logs

    def clear_logs_pernamently(self):
        self.all_of_logs = []

    def clock_working(self):
        return self.now

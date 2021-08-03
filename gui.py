from root import TheOffice
class GUI:
    def __init__(self):

        self.my_office = TheOffice("MROK")
        self.__still_on = True
        self.main_loop()
        self.my_office.add_log("Start")
        print("Welcome")

    def main_loop(self):
        while self.__still_on == True:
            self.print_menu()
            self.way = int(input("What's next?: "))
            print("\n\n\n")

            if self.way == 1:
                self.my_office.show_workers()

            if self.way == 2:
                name = self.input_name()
                surname = self.input_surname()
                self.my_office.add_worker(name, surname)

            if self.way == 3:
                self.my_office.show_logs()

            if self.way == 4:
                name = input("Name: ")
                surname = input("Surname: ")
                email = input("Email: ")
                self.my_office.set_email_for_worker(name, surname, email)

            if self.way == 5:
                self.my_office.clear_logs_pernamently()

            if self.way == 6:
                self.my_office.count_salary_for_everyone()

            if self.way == 7:
                name = input("Name: ")
                surname = input("Surname: ")
                salary = int(input("Salary: "))
                self.my_office.set_salary_for_worker(name, surname, salary)

            if self.way == 8:
                name = input("Name: ")
                surname = input("Surname: ")
                hours = int(input("Hours: "))
                self.my_office.add_hour_worker(name, surname, hours)

            if self.way == 9:
                name = input("Name: ")
                surname = input("Surname: ")
                self.my_office.rem_worker(name, surname)

            if self.way == 0:
                self.my_office.safe_logs_to_file()
                self.my_office.safe_workers_to_file()
                self.__still_on = False

    def print_menu(self):
        print(f"\n...:::Menu:::...  "
              f"\n\n::1:.. Show Workers\n"
              f"::2:.. Add worker\n"
              f"::3:.. Show Logs\n"
              f"::4:.. Clear Logs\n"
              f"::5:.. Add worker\n"
              f"::6:.. Show Logs\n"
              f"::7:.. Clear Logs\n"
              f"::8:.. Clear Logs \n"
              f"::9:.. Clear Logs\n"
              f"\n::0:.. Exit & Save\n\n")

    def worker_input_name(self):
        name = input("Name: ")
        return f"{name}"

    def input_name(self):
        name = input("Name: ")
        return name

    def input_surname(self):
        surname = input("Surname: ")
        return surname

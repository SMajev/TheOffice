from root import TheOffice


class Main:
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
                name = input("Name: ")
                surname = input("Surname: ")
                self.my_office.add_worker(name, surname)

            if self.way == 3:
                self.my_office.show_logs()

            if self.way == 5:
                self.my_office.clear_logs_pernamently()

            if self.way == 0:
                self.my_office.safe_logs_to_file()
                self.my_office.safe_workers_to_file()
                self.__still_on = False

    def print_menu(self):
        print(f"\n...:::Menu:::...  "
              f"\n\n:1:.. Show Workers\n"
              f":2:.. Add worker\n"
              f":3:.. Show Logs\n"
              f":5:.. Clear Logs\n\n"
              f"\n:0:.. Exit & Save\n\n")

    def worker_input_name(self):
        name = input("Name: ")
        return f"{name}"


if __name__ == "__main__":
    my_main = Main()

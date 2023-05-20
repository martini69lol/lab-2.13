class FlightManager:
    def init(self):
        self.airport = []

    def add_flight(self):
        race = input("Название пункта назначения рейса: ")
        number = input("Номер рейса: ")
        type = float(input("Тип самолёта: "))

        airports = {
            'race': race,
            'number': number,
            'type': type,
        }

        self.airport.append(airports)
        if len(self.airport) > 1:
            self.airport.sort(key=lambda item: item.get('race', ''))

    def list_flights(self):
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "No",
                "Пункт",
                "Номер",
                "Тип самолёта."
            )
        )
        print(line)

        for idx, airports in enumerate(self.airport, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    airports.get('race', ''),
                    airports.get('number', ''),
                    airports.get('type', 0)
                )
            )

        print(line)

    def select_flight(self, sel):
        count = 0
        for airports in self.airport:
            if airports.get('type') == sel:
                count += 1
                print(
                    '{:>4}: {}'.format(count, airports.get('race', ''))
                )
                print('Пункт:', airports.get('race', ''))
                print('Номер:', airports.get('number', ''))

        if count == 0:
            print("Тип самолета не найден.")

    def help(self):
        print("Список команд:\n")
        print("add - добавить рейс;")
        print("list - вывести список рейсов;")
        print("select <товар> - информация о рейсе;")
        print("help - отобразить справку;")
        print("exit - завершить работу с программой.")


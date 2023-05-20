from lab_package import FlightManager

if name == 'main':
    manager = FlightManager()

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            manager.add_flight()
        elif command == 'list':
            manager.list_flights()
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            sel = parts[1]
            manager.select_flight(sel)
        elif command == 'help':
            manager.help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

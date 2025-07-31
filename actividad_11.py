owners = {}
plate = {}

while True:
    print(f"\n- MENÚ DE CARRO E IMPUESTOS -")
    print(f"1. Agregar propietarios")
    print(f"2. Mostrar propietarios")
    print(f"3. Buscar propietario")
    print(f"4. Historial de vehículos")
    print(f"5. Salir")

    num_user = input(f"\nIngrese la opción a la que desea ir: ")

    match num_user:
        case "1":
            print("\nAgregar propietarios")
            num_owners = int(input(f"¿Cuántos propietarios va a ingresar?: "))

            for i in range(num_owners):
                print(f"Propietario #{i+1}")

                while True:
                    nit_owner = input(f"Ingrese el NIT del propietario: ")
                    if nit_owner not in owners:
                        break
                    else:
                        print(f"NIT ya registrado, intente nuevamente.")
                name_owner = input(f"Ingrese el nombre del propietario: ")
                phone_owner = input(f"Ingrese el telefono del propietario: ")
                count_owner = int(input(f"Ingrese la cantidad de vehículos del propietario: "))

                owners[nit_owner] = {
                    "name": name_owner,
                    "phone": phone_owner,
                    "vehicle": {}
                }

                for j in range(count_owner):
                    print(f"Vehículo #{j+1}")
                    plate_car = input(f"Ingrese la placa del vehículo: ")
                    make_car = input(f"Ingrese la marca del vehículo: ")
                    model_car = input(f"Ingrese el modelo del carro: ")
                    year_car = input(f"Ingrese el año del carro: ")
                    tax_car = input(f"¿Pago el impuesto? (si / no) ").lower()

                    plate[plate_car] = {
                        "make": make_car,
                        "model": model_car,
                        "year": year_car,
                        "tax": tax_car
                    }

                    owners[nit_owner]["vehicle"][plate_car] = plate[plate_car]

        case "2":
            print(plate)
            print(owners)
            count = 1
            for nit_owner, data in owners.items():
                print(f"\nPropietario #{count}")
                print(f"NIT del propietario {nit_owner}")
                print(f"Nombre del propietario: {data['name']}")
                print(f"Número del propietario: {data['phone']}")
                print(f"Vehículos: ")
                for placa, info in data['vehicle'].items():
                    print(
                        f"- Placa: {placa.upper()} | {info['make']} {info['model']} ({info['year']}) | Impuestos: {info['tax']}")
                count += 1
        case "3":
            print("\nBuscar propietario")

        case "4":
            print("\nHistorial de vehículos")

        case "5":
            print("\nSaliendo del programa")
            break

        case _:
            print(f"Valor inválido, intente de nuevo.")
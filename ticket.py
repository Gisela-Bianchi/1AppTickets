import random
import pickle
import os
#donde se guardan los tickets
archivo_tickets = "tickets.pkl"
#se cargan los tickets al iniciar el programa
if os.path.isfile(archivo_tickets):
    with open(archivo_tickets, "rb") as f:
        tickets = pickle.load(f)
else:
 tickets = []

while True:
    print("\n")
    print("Hola bienvenido al sistema de Tickets\n")
    print("==============================")
    print("1. Generar un Nuevo Ticket   |")
    print("2. Leer un Ticket            |")
    print("0. Salir                     |")
    print("==============================")
    try:
        opcion = int(input("Por favor, selecciona una opcion: "))
    except ValueError:
        print("Por favor, ingrese una opcion valida (1, 2 o 0).")
        continue

    if opcion == 1:  # Alta ticket
        # Delegar a la persona encargada de la Parte 2
        pass

    elif opcion == 2:  # Leer ticket
        # Delegar a la persona encargada de la Parte 3
        pass

    elif opcion == 0:  # Salir
        print("Guardando tickets...")
        with open(archivo_tickets, "wb") as f:
            pickle.dump(tickets, f)
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida")


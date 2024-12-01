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

    if opcion == 1:  # Alta ticket, comentario 2
        seguir = "s"
        while seguir == "s":
            nombre = input("Ingrese su Nombre: ")
            sector = input("Ingrese su Sector: ")
            asunto = input("Ingrese Asunto: ")
            problema = input("Ingrese un Mensaje: ")
            numero = random.randint(1000, 9999)
 
            ticket = [nombre, sector, asunto, problema, numero]
            tickets.append(ticket)
 
 
 
            print("======================================")
            print("Se genero el siguiente Ticket")
            print("======================================")
            print("Su nombre:", ticket[0], "    NºTicket:", ticket[4])
            print("Sector:", ticket[1])
            print("Asunto:", ticket[2])
            print("Mensaje:", ticket[3])
            print("        Recordar su numero de Ticket")
 
            seguir = input("¿Desea generar un nuevo Ticket? (s/n): ").lower()
            while seguir not in ("s", "n"):
                print("Por favor, ingresa una letra correcta (s o n).")
                seguir = input("¿Quieres registrar un nuevo ticket? (s/n): ").lower()

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


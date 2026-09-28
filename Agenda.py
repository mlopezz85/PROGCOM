# Agenda de actividades JAMM

agenda = []

while True:
    print("\n--- AGENDA ---")
    print("1. Ver agenda")
    print("2. Agregar actividad")
    print("3. Buscar actividad")
    print("4. Eliminar actividad")
    print("5. Mostrar cantidad de actividades")
    print("6. Ver primera actividad")
    print("7. Ver última actividad")
    print("8. Ordenar agenda")
    print("9. Salir")

    opcion = input("\nSelecciona una opción (1-9): ").strip()

    if opcion == "1":
        if not agenda:
            print("La agenda está vacía.")
        else:
            print("\nLista de actividades:")
            for i, actividad in enumerate(agenda, 1):
                print(f"{i}. {actividad}")

    elif opcion == "2":
        actividad = input("Ingrese la nueva actividad: ").strip()
        if actividad:
            agenda.append(actividad)
            print(f"Actividad '{actividad}' agregada correctamente.")
        else:
            print("No se puede agregar una actividad vacía.")

    elif opcion == "3":
        actividad = input("Ingrese la actividad a buscar: ").strip()
        if actividad in agenda:
            posicion = agenda.index(actividad) + 1
            print(f"La actividad '{actividad}' se encuentra en la posición {posicion}.")
        else:
            print(f"La actividad '{actividad}' no está en la agenda.")

    elif opcion == "4":
        actividad = input("Ingrese la actividad a eliminar: ").strip()
        if actividad in agenda:
            agenda.remove(actividad)
            print(f"Actividad '{actividad}' eliminada con éxito.")
        else:
            print(f"La actividad '{actividad}' no existe en la agenda.")

    elif opcion == "5":
        print(f"Total de actividades en la agenda: {len(agenda)}")

    elif opcion == "6":
        if agenda:
            print(f"Primera actividad: {agenda[0]}")
        else:
            print("La agenda está vacía.")

    elif opcion == "7":
        if agenda:
            print(f"Última actividad: {agenda[-1]}")
        else:
            print("La agenda está vacía.")

    elif opcion == "8":
        if agenda:
            agenda.sort()
            print("Agenda ordenada alfabéticamente correctamente.")
        else:
            print("La agenda está vacía, nada que ordenar.")

    elif opcion == "9":
        print("¡Gracias por usar la agenda! Hasta luego.")
        break

    else:
        print("Opción no válida. Por favor, seleccione un número entre 1 y 9.")
# Agenda de actividades JAMM
agenda = {}
contador = 1

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
            print("\nActividades:")
            for clave, actividad in agenda.items():
                print(f"{clave}. {actividad}")

    elif opcion == "2":
        actividad = input("Ingrese la nueva actividad: ").strip()

        if actividad:
            agenda[contador] = actividad
            contador += 1
            print("Actividad agregada correctamente.")
        else:
            print("No se puede agregar una actividad vacía.")

    elif opcion == "3":
        actividad = input("Ingrese la actividad a buscar: ").strip()

        if actividad in agenda.values():
            for clave, valor in agenda.items():
                if valor == actividad:
                    print(f"La actividad está en la posición {clave}.")
                    break
        else:
            print("La actividad no está en la agenda.")

    elif opcion == "4":
        actividad = input("Ingrese la actividad a eliminar: ").strip()

        clave_eliminar = None

        for clave, valor in agenda.items():
            if valor == actividad:
                clave_eliminar = clave
                break

        if clave_eliminar is not None:
            del agenda[clave_eliminar]
            print("Actividad eliminada con éxito.")
        else:
            print("La actividad no existe.")

    elif opcion == "5":
        print(f"Total de actividades: {len(agenda)}")

    elif opcion == "6":
        if agenda:
            primera = next(iter(agenda.values()))
            print(f"Primera actividad: {primera}")
        else:
            print("La agenda está vacía.")

    elif opcion == "7":
        if agenda:
            ultima = list(agenda.values())[-1]
            print(f"Última actividad: {ultima}")
        else:
            print("La agenda está vacía.")

    elif opcion == "8":
        if agenda:
            actividades = sorted(agenda.values())
            agenda = {
                i + 1: actividad
                for i, actividad in enumerate(actividades)
            }
            contador = len(agenda) + 1
            print("Agenda ordenada alfabéticamente.")
        else:
            print("La agenda está vacía.")

    elif opcion == "9":
        print("¡Gracias por usar la agenda! Hasta luego.")
        break

    else:
        print("Opción no válida.")
from linkedList import linkedList

lista = linkedList()

class Menu:
    while True:
        print("Menu:")
        print("1. Insertar Datos")
        print("2. Mostrar Lista")
        print("3. Ordenar Datos")
        print("4. Mostrar Resultado Ordenado")
        print("5. Salir")
        result = None
        opcion = int(input("Selecciona la opción: "))
        if (opcion == 1):
            while result is None and result is not (1 or 2 or 3):
                data = int(input("Digita el dato a ingresar:"))
                print("1. Insertar al Inicio ")
                print("2. Insertar al Final ")
                print("3. Insertar en posición deseada ")
                result = int(input("Selecciona la opción: "))
                if result == 1:
                    lista.insert_at_beginning(data)
                elif result == 2:
                    lista.insert_at_end(data)
        elif opcion == 2:
            lista.recorrer()
        elif opcion == 3:
            lista.ordenar()
        elif opcion == 4:
            lista.recorrerOrdenado()
        elif opcion == 5:
            break



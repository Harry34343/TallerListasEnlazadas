from linkedList import linkedList

lista = linkedList()

class Menu:
    while True:
        print("Menu:")
        print("1. Insertar Datos")
        print("2. Mostrar Lista")
        print("3. Buscar Dato")
        print("4. Eliminar Primer Elemento")
        print("5. Eliminar Por Valor")
        print("6. Tamaño de la Lista")
        print("7. Invertir Lista")
        print("8. Ordenar Lista")
        print("9. Salir")
        result = None
        opcion = int(input("Selecciona la opción: "))
        if (opcion == 1):
            data = int(input("Digita el dato a ingresar:"))
            while result is None or (result != 1 and result !=2):
                print("1. Insertar al Inicio ")
                print("2. Insertar al Final ")
                result = int(input("Selecciona la opción: "))
                if result == 1:
                    lista.insert_at_beginning(data)
                elif result == 2:
                    lista.insert_at_end(data)
        elif opcion == 2:
            lista.Mostrar()
        elif opcion == 3:
            val = int(input("Digite el valor a buscar: "))
            x =lista.Search(val)
            print("El dato se encuentra en la posición: "+str(x))
        elif opcion == 4:
            lista.DeleteFirst()
        elif opcion == 5:
            val = int(input("Digite el valor a eliminar: "))
            lista.DeleteByValor(val)
        elif opcion == 6:
            print("Tamaño de la lista:", lista.size())
        elif opcion == 7:
            lista.Invertir()
        elif opcion == 8:
            lista.Ordenar()
        elif opcion == 9:
            break



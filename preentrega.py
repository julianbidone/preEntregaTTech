inventario = []
opcion = 0

while opcion != 5:
    print("\nMenu de gestion de productos \n")
    print("1. Registro: Alta de productos nuevos.")
    print("2. Visualizacion: Consulta de inventario.")
    print("3. Actualizacion: Modificar la cantidad en stock de un producto o su precio.")
    print("4. Eliminacion: Dar de baja productos.")
    print("5. Salir.")
    
    try:
        opcion = int(input("\nSeleccione una opcion: "))
        print(f"\nUsted selecciono la opcion Nro: {opcion}\n")

        if opcion == 1:
            while True:
                nombre = str(input("Ingrese el nombre del producto a agregar: "))       
                while True:
                    try:
                        precio = float(input(f"Ingrese el precio unitario de {nombre}: "))
                        if precio <= 0:
                            print("Ingrese un precio mayor a 0.")
                        else:break
                    except ValueError:
                        print("El precio debe ser un numero")
                        
                while True:
                    try:
                        cantidad = int(input(f"Ingrese la cantidad de {nombre} que desea agregar: "))
                        if cantidad <= 0:
                            print("Ingrese una cantidad valida.")
                        else:break
                    except ValueError:
                        print("La cantidad debe ser un numero")
                producto = [nombre.upper(),precio ,cantidad]        
                inventario.append(producto)
                print("Producto cargado con exito!\n")
                
                seguir = input("Desea agregar otro producto? (s:si n:no): ").lower()
                if seguir != "s":
                    break                
        elif opcion == 2:
            if not inventario:
                print("No hay productos registrados.")
            else:
                print("\nListado de Inventario\n")
                print("-"*60)
                for producto in inventario:
                    print(f"Nombre del Producto: {producto[0]}\t Precio: {producto[1]}\t Cantidad: {producto[2]}")
                    print("-"*60)

        elif opcion == 3:
            producto = str(input("Ingrese el nombre del producto que desea modificar: ")).upper()
            i = 0
            encontrado = -1  # Usar -1 para indicar que el producto no se ha encontrado
            # Bucle de búsqueda
            while i < len(inventario) and encontrado == -1:
                if inventario[i][0] == producto:
                    encontrado = i
                i += 1

            if encontrado != -1:
                modificar = 0
                print("Se encontró el producto.\nIngrese qué campo quiere modificar:\n 1. Precio \n 2. Cantidad")
                while modificar <= 0:
                    modificar = int(input("Ingrese una opción: "))
                    if modificar <= 0:
                        print("Ingrese una opción válida.")
                    elif modificar == 1:    
                        while True:
                            try:
                                precio = float(input(f"Ingrese el nuevo precio: "))
                                if precio <= 0:
                                    print("Ingrese un precio mayor a 0.")
                                else:break
                            except ValueError:
                                print("El precio debe ser un numero")
                        inventario[encontrado][1] = precio 
                    elif modificar == 2:
                        while True:
                            try:
                                cantidad = int(input(f"Ingrese la cantidad de stock que hay: "))
                                if cantidad < 0:
                                    print("Ingrese una cantidad valida.")
                                else:break
                            except ValueError:
                                print("La cantidad debe ser un numero")
                        inventario[encontrado][2] = cantidad
                    else:
                        print("Opción no válida.")
            else:
                print(f"No se encontró el producto {producto}")
        elif opcion == 4:
            producto = str(input("Ingrese el nombre del producto que desea eliminar: ")).upper()
            i = 0
            encontrado = -1  # Usar -1 para indicar que el producto no se ha encontrado
            # Bucle de búsqueda
            while i < len(inventario) and encontrado == -1:
                if inventario[i][0] == producto:
                    encontrado = i
                i += 1
            if encontrado !=-1:
                inventario.pop(encontrado)
                print(f"El producto {producto} ah sido eliminado del inventario.")
            else:
                print("No se encontro el producto")
            
    except ValueError:
        print("Entrada no valida. Por favor ingrese un valor numerico del 1 al 5.")
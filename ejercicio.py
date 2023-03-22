# valores iniciales
import sys


clientes = []
productos = []

#1 crear cliente
def crear_cliente():
    # pregunto los datos
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    clientId = len(clientes) + 1
    # agrego el cliente a la lista
    clientes.append([clientId, nombre, apellido])
    print("Cliente creado!")

#2 crear productos
def crear_producto():
    # pregunto los datos
    producto = input("Ingrese el producto: ")
    valor = float(input("Ingrese el valor: "))
    productId = len(productos) + 1
    categoria = input("Categoría del producto: ")
    # agrego el producto a la lista
    productos.append([productId, producto, valor, categoria])

#3 consultar cliente por id
def consultar_cliente_por_id():
    id_cliente = int(input("ID de cliente: "))
    for cliente in clientes:
        #print(cliente[0])#si dejo esto imprime todos los id clientes
        if id_cliente == cliente[0]:
            print(f'El nombre del cliente es {cliente[1]}, su apellido es {cliente[2]} y el id {cliente[0]}')


#4 buscar clientes por nombre/apellido
def consultar_cliente_por_nombre_apellido():
    found = False
    nombre_apellido = input("¿Qué desea buscar? nombre / apellido: ")
    if nombre_apellido == "nombre":
        nombre = input("Ingrese el nombre del cliente: ") # 'mag'
        for cliente in clientes:
            if nombre == cliente[1]:
                print('Se ha encontrado el cliente')
                found = True
                print(cliente)
                return
            
    elif nombre_apellido == "apellido":
        apellido = input("Ingrese el apellido del cliente: ")
        for cliente in clientes:
            if apellido == cliente[2]:
                print('Se ha encontrado el cliente')
                found = True
                print(cliente) 

    elif nombre_apellido != 'nombre' or nombre_apellido != 'apellido':
        print("Ingrese una opción válida!")
        return # este return temprano hace que se corte la función

    # este if se pregunta siempre, no depende de los elif anteriores
    if found is False:
        print('No se ha encontrado cliente')

#5 borrar cliente
def borrar_cliente():
    opcion_elegir: input("Desea borrar cliente por nombre, apellido o id?: (n / a / id) ")
    if opcion_elegir == "n":
        nombre_buscar = input("Ingrese el nombre del usuario que desea borrar: ")
        borrar_cliente_por_nombre(nombre_buscar)
    elif opcion_elegir == "a":
        apellido_buscar = input("Ingrese el apellido del usuario que desea borrar: ")
        borrar_cliente_por_apellido(apellido_buscar)    
    elif opcion_elegir == "id":
        id_buscar = int(input("Ingrese el id del usuario que desea borrar: "))
        borrar_cliente_por_id(id_buscar)
    else:
        # el usuario no eligio ni "n", "a", o "id"
        print("por favor, elegir n, a o id")
        
    #funcion para borrar cliente por nombre        
def borrar_cliente_por_nombre(nombre):
    #recorro la lista de clientes
    for cliente in clientes:
        if cliente[1] == nombre:
            clientes.remove(cliente)
            break
        else:
            continue
        

#funcion para borrar cliente por id    
def borrar_cliente_por_id(ID):
    #recorro la lista por codigo
    for cliente in clientes:
        if cliente[0] == ID:
            clientes.remove(cliente)
            break #cuando encuentra el cliente(el 1° solo), rompe el ciclo
        else:  # es para aclarar el codigo
            continue

#funcion para borrar cliente por apellido
def borrar_cliente_por_apellido(a):
    #recorro la lista por apellido
    for clientes in clientes:
        if cliente[2] == a:
            clientes.remove(cliente)
            break #por que este break y continue
        else: 
            continue
        
#6 borrar producto por nombre
def borrar_producto_nombre(nombre):
    #recorro la lista de productos
    for producto in productos:
        if producto[0] == nombre:
            productos.remove(producto)
        else:
            continue
        
#7 imrpimir clientes
def imprimir_clientes():
    for cliente in clientes:
        print(cliente)
     
#8 imprimir productos
def imprimir_productos():
    for producto in productos:
        print(producto)
    
# menu principal
while True:
    texto_inicio = """ MENU PRINCIPAL.

    Elija una opcion:
    1-Crear cliente
    2-Crear producto
    3-Consultar cliente por ID
    4-Buscar cliente por nombre/apellido
    5-Borrar cliente por nombre/apellido/ID
    6-Borrar producto
    7-Imprimir lista de clientes
    8-Imprimir lista de productos

    Para finalizar, presione N """

    print(texto_inicio)


    opcion_elegir = input("Ingrese una opción: ")
    print(f'Se eligio {opcion_elegir=}')
    if opcion_elegir.isdigit() is False:
        if opcion_elegir == "n" or opcion_elegir == "N":
            # cierro el programa
            sys.exit()
        else:
            print("por favor elegir una de las opciones 1 a 8")
            continue
    else:
        opcion_elegir = int(opcion_elegir)


        if opcion_elegir == 1:
            crear_cliente()

        elif opcion_elegir == 2:
            crear_producto()
                
        elif opcion_elegir == 3:
            consultar_cliente_por_id()

        elif opcion_elegir == 4:
            consultar_cliente_por_nombre_apellido()

        elif opcion_elegir == 5:
            borrar_cliente()

        elif opcion_elegir == 6:
            borrar_producto_nombre()

        elif opcion_elegir == 7:
            imprimir_clientes()

        elif opcion_elegir == 8:
            imprimir_productos()
            
        else:
            break

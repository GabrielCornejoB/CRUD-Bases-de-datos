#METODOS DE CATEGORIAS
def Mostrar_categorias(categorias):
    print("\nCategorias: \n")
    print("| ID | Categoria")
    print("|----|-----------------------")
    for c in categorias:
        if c[0] < 10:
            datos = "| {}  | {}"
        else:
            datos = "| {}  | {}"
        print(datos.format(c[0], c[1]))

def Pedir_datos_registro():
    id_cat = int(input("Ingrese ID de la categoria: "))   
    desc_cat = input("Ingrese nombre de la categoria: ")

    if id_cat > 0 and id_cat < 100 and len(desc_cat) > 0 and len(desc_cat) <= 25:  
        categoria = (id_cat, desc_cat)
        return categoria
    else:
        print("\nLos datos ingresados no son validos")

def Pedir_datos_actualizacion(categorias):
    Mostrar_categorias(categorias)
    id_editar = int(input("\nIngrese el ID de la categoria que desea actualizar: "))
    existe_codigo = False
    for c in categorias:
        if(int(c[0]) == id_editar):
            existe_codigo = True
            break  
    if existe_codigo:
        desc_cat = input("Ingrese el nuevo nombre de la categoria: ")
        if len(desc_cat) > 0 and len(desc_cat) <= 25:  
            categoria = (id_editar, desc_cat)
        else:
            print("\nLos datos ingresados no son validos")
    else:
        categoria = None
    return categoria

def Pedir_datos_eliminacion(categorias):
    Mostrar_categorias(categorias)
    id_eliminar = int(input("\nIngrese el ID de la categoria que desea eliminar: "))
    existe_codigo = False
    for c in categorias:
        if(int(c[0]) == id_eliminar):
            existe_codigo = True
            break  
    if not existe_codigo:
        id_eliminar = 0  
    return id_eliminar

#METODOS DE PRODUCTOS
def Mostrar_productos(productos):
    print("\nProductos: \n")
    print("| ID | Precio | Producto")
    print("|----|--------|---------------------------")
    for p in productos:
        if p[0] >= 10:
            if(len(p[2]) == 3):
                datos = "| {} | ${}   | {}"
            elif(len(p[2]) == 4):
                datos = "| {} | ${}  | {}"
            elif len(p[2]) == 5:
                datos = "| {} | ${} | {}"
            else:
                datos = "| {} | ${}| {}"
        else:
            if(len(p[2]) == 3):
                datos = "| {}  | ${}   | {}"
            elif(len(p[2]) == 4):
                datos = "| {}  | ${}  | {}"
            elif len(p[2]) == 5:
                datos = "| {}  | ${} | {}"
            else:
                datos = "| {}  | ${}| {}"
        print(datos.format(p[0], p[2], p[1]))

def Pedir_datos_registroP(categorias):
    id_p = int(input("\nIngrese ID del producto: "))   
    desc_p = input("Ingrese nombre del producto: ")
    Mostrar_categorias(categorias)
    id_c = int(input("\nIngrese el ID de la categoria a la que pertenece el producto: "))
    precio = input("Ingrese el precio del producto: ")

    existe_codigo = False
    for c in categorias:
        if(int(c[0]) == id_c):
            existe_codigo = True
            break
    if id_p > 0 and len(desc_p) > 0 and len(desc_p) <= 50 and existe_codigo == True and len(precio) <=6:  
        producto = (id_p, desc_p, id_c, precio)
        return producto
    else: 
        print("\nLos datos ingresados no son validos")

def Pedir_datos_actualizacionP(productos):
    Mostrar_productos(productos)
    id_editar = int(input("\nIngrese el ID del producto que desea actualizar: "))
    existe_codigo = False
    for p in productos:
        if(int(p[0]) == id_editar):
            existe_codigo = True
            break  
    if existe_codigo:
        desc_p = input("Ingrese el nuevo nombre del producto: ")
        precio = input("Ingrese el nuevo precio del producto: ")
        if len(desc_p) > 0 and len(desc_p) <= 25 and len(precio) <=6 and existe_codigo:  
            producto = (id_editar, desc_p, precio)
        else:
            print("\nLos datos ingresados no son validos")
    else:
        producto = None
    return producto

def Pedir_datos_eliminacionP(productos):
    Mostrar_productos(productos)
    id_eliminar = int(input("\nIngrese el ID del producto que desea eliminar: "))
    existe_codigo = False
    for p in productos:
        if(int(p[0]) == id_eliminar):
            existe_codigo = True
            break  
    if not existe_codigo:
        id_eliminar = 0  
    return id_eliminar
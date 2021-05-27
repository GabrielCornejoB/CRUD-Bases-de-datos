from BD.conexion import Data_Access_Object as DAO
import operaciones
import tkinter as tk
from tkinter import ttk

def Menu_Principal():
    continuar = True
    while(continuar):
        opcion_correcta = False
        while(not opcion_correcta):
            print("-----MENU PRINCIPAL-----")  
            print("1. Tabla Categorias")  
            print("2. Tabla Productos")
            print("3. Salir de la aplicacion\n")
            opcion = int(input("Elija una opcion: "))

            if(opcion < 1 or opcion > 3):
                print("\nOpcion incorrecta\n")
            elif opcion == 3:
                continuar = False
                print("\nSalio de la aplicacion exitosamente\n")  
                break 
            elif opcion == 1:
                continuarC = True
                while(continuarC):
                    opcion_correctaC = False
                    while(not opcion_correctaC):
                        print("-----CATEGORIAS-----")
                        print("1. Listar categorias")
                        print("2. Registrar categorias")
                        print("3. Actualizar categorias")
                        print("4. Eliminar categorias")
                        print("5. Salir\n")
                        opcionC = int(input("Seleccione una opcion: "))

                        if(opcionC<1 or opcionC>5):
                            print("\nOpcion incorrecta\n")
                        elif opcionC == 5:
                            continuarC = False
                            print("\nSalio al menu principal\n")  
                            break             
                        else:
                            opcion_correctaC = True
                            Ejecutar_Opcion_Categorias(opcionC)
            elif opcion == 2:
                continuarP = True
                while(continuarP):
                    opcion_correctaP = False
                    while(not opcion_correctaP):
                        print("-----PRODUCTOS-----")
                        print("1. Listar productos")
                        print("2. Registrar productos")
                        print("3. Actualizar productos")
                        print("4. Eliminar productos")
                        print("5. Salir\n")
                        opcionP = int(input("Seleccione una opcion: "))

                        if(opcionP<1 or opcionP>5):
                            print("\nOpcion incorrecta\n")
                        elif opcionP == 5:
                            continuarP = False
                            print("\nSalio al menu principal\n")  
                            break             
                        else:
                            opcion_correctaP = True
                            Ejecutar_Opcion_Productos(opcionP)

def Ejecutar_Opcion_Categorias(opcion):
    dao = DAO()
    if opcion == 1:
        try:
            categorias = dao.Mostrar_categorias()
            if (len(categorias) > 0):
                operaciones.Mostrar_categorias(categorias)
            else:
                print("No se encontraron categorias")
        except:
            print("Ocurrio un error")
    elif opcion == 2:
        categoria = operaciones.Pedir_datos_registro()
        try:
            dao.Crear_categoria(categoria)
        except:
            print("Ocurrio un error en la creacion de una categoria\n")
    elif opcion == 3:
        try:
            categorias = dao.Mostrar_categorias()
            if (len(categorias) > 0):              
                categoria = operaciones.Pedir_datos_actualizacion(categorias)
                if categoria:
                    dao.Actualizar_categoria(categoria)
                else:
                    print("Codigo de categoria a actualizar no encontrado\n")
            else:
                print("No se encontraron categorias\n")
        except:
            print("Ocurrio un error en la actualizacion de una categoria\n")
    elif opcion == 4:
        try:
            categorias = dao.Mostrar_categorias()
            if (len(categorias) > 0):
                codigoEliminar = operaciones.Pedir_datos_eliminacion(categorias)
                if not(codigoEliminar == 0):
                    dao.Eliminar_categoria(codigoEliminar)
                else:
                    print("Codigo de categoria no encontrado\n")
            else:
                print("No se encontraron categorias\n")
        except:
            print("Ocurrio un error en la eliminacion de una categoria\n")
    else:
        print("Opcion incorrecta")

def Ejecutar_Opcion_Productos(opcion):
    dao = DAO()
    if(opcion == 1):
        try:
            productos = dao.Mostrar_productos()
            if (len(productos) > 0):
                operaciones.Mostrar_productos(productos)
            else:
                print("No se encontraron productos")
        except:
            print("Ocurrio un error")
    elif opcion == 2:              
        try:
            categorias = dao.Mostrar_categorias()
            if(len(categorias) > 0):
                producto = operaciones.Pedir_datos_registroP(categorias)
                dao.Crear_producto(producto)
        except:
            print("Ocurrio un error en la creacion de un producto\n")  
    elif(opcion == 3):
        try:
            productos = dao.Mostrar_productos()
            if (len(productos) > 0):              
                producto = operaciones.Pedir_datos_actualizacionP(productos)
                if producto:
                    dao.Actualizar_producto(producto)
                else:
                    print("Codigo de producto a actualizar no encontrado\n")
            else:
                print("No se encontraron productos\n")
        except:
            print("Ocurrio un error en la actualizacion de un producto\n")
    elif(opcion == 4):
        try:
            productos = dao.Mostrar_productos()
            if (len(productos) > 0):
                codigoEliminar = operaciones.Pedir_datos_eliminacionP(productos)
                if not(codigoEliminar == 0):
                    dao.Eliminar_producto(codigoEliminar)
                else:
                    print("Codigo de categoria no encontrado\n")
            else:
                print("No se encontraron categorias\n")
        except:
            print("Ocurrio un error en la eliminacion de una categoria\n")
    else:
        print("Opcion incorrecta") 
    
Menu_Principal()
'''
dao = DAO()
#Se crea la ventana y se le pasan los parametros de configuracion
window = tk.Tk()                        #Se crea una nueva instancia
window.title('Menu principal')          #Se le coloca un titulo
window.geometry("1080x480")              #Se le asigna la resolución
window.configure(bg="azure")            #Se le coloca el color de fondo
window.resizable(0,0)                   #Se bloquea que se pueda aumentar o disminuir el tamaño de la ventana
#----------------------------------------------------------------------

#Creación de labels
titulo = tk.Label(text="Base de Datos del Minimercado", fg= "DodgerBlue4", bg = "azure", font=("Verdana 26 bold italic")).place(x=20,y=20)
lbl_categorias = tk.Label(text="Categorias:", fg= "black", bg = "azure", font=("Verdana 15 italic"), height=2).place(x=20, y=75)
lbl_productos = tk.Label(text="Productos:", fg= "black", bg = "azure", font=("Verdana 15 italic"), height=2).place(x=250, y=75)
#----------------------------------------------------------------------

#Creación de listbos
lb_categorias = tk.Listbox(bg='Lightblue1', width = 18, height = 10, yscrollcommand = True, font=("Verdana 12"))   
lb_categorias.place(x=20, y=120)
lb_productos = tk.Listbox(bg='Lightblue1', width = 38, height = 10, yscrollcommand = True, font=("Verdana 12"))
lb_productos.place(x=250, y=120)
#----------------------------------------------------------------------
       
#Se crean los botones de categorias
btn_crear_c = tk.Button( text="Crear categoria", font=("Verdana, 14"), bg='DodgerBlue3', fg='ghost white', width=15, bd = 4, activebackground='steel blue').place(x=20, y=325)
btn_editar_c = tk.Button(text="Editar categoria", font=("Verdana, 14"), bg='DodgerBlue3', fg='ghost white', width=15, bd = 4,activebackground='steel blue').place(x=20, y=375)
btn_eliminar_c = tk.Button(text="Borrar categoria", font=("Verdana, 14"), bg='DodgerBlue3', fg='ghost white', width=15, bd = 4, activebackground='steel blue').place(x=20, y=425)
#----------------------------------------------------------------------

#Se crean los botones de productos
btn_crear_p = tk.Button(text="Crear producto", font=("Verdana, 14"), bg='DodgerBlue3', fg='ghost white', width=15, bd = 4, activebackground='steel blue').place(x=250, y=325)
btn_editar_p = tk.Button(text="Editar producto", font=("Verdana, 14"), bg='DodgerBlue3', fg='ghost white', width=15, bd = 4, activebackground='steel blue').place(x=250, y=375)
btn_eliminar_p = tk.Button(text="Borrar producto", font=("Verdana, 14"), bg='DodgerBlue3', fg='ghost white', width=15, bd = 4, activebackground='steel blue').place(x=250, y=425)
#----------------------------------------------------------------------

#btn_actualizar = tk.Button(text="Actualizar", font=("Verdana, 14"), bg='DodgerBlue3', fg='ghost white', width=15, bd = 4, activebackground='steel blue').place(x=500, y=425)
lbl_nidcat = tk.Label(text="Crear categoria",bg = "azure").place(x=940,y=20)
txt_idcat = tk.Entry(bg = "Lightblue1")
idcat = int(txt_idcat.get())
txt_idcat.place(x=940,y=40)
txt_nombrecat = tk.Entry(bg = "Lightblue1")
desccat = txt_nombrecat.get()
txt_nombrecat.place(x=940,y=60)

def Crear_cat():
    nueva_cat = operaciones.Pedir_datos_registro(idcat,desccat)
    dao.Crear_categoria(nueva_cat)
    Actualizar_bd()

btn_crearcat = tk.Button(command=Crear_cat,text="REGISTRAR").place(x=940,y=80)

def Actualizar_bd():
    categorias = dao.Mostrar_categorias()  
    lb_categorias.insert('end', *operaciones.Mostrar_categorias(categorias))
    productos = dao.Mostrar_productos()
    lb_productos.insert('end', *operaciones.Mostrar_productos(productos))

#Se cargan los listbox con las categorias y productos ya creados
categorias = dao.Mostrar_categorias()  
lb_categorias.insert('end', *operaciones.Mostrar_categorias(categorias))
productos = dao.Mostrar_productos()
lb_productos.insert('end', *operaciones.Mostrar_productos(productos))
#----------------------------------------------------------------------

window.mainloop()
'''
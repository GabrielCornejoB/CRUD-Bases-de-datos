import mysql.connector
from mysql.connector import Error

#Conexión a la base de datos
class Data_Access_Object():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                port=3306,
                user='root',
                password='guarito123',
                db='minimercado'
            )
        except Error as e:
            print("Error al intentar la conexión: {}".format(e))

    #METODOS DE CATEGORIAS
    def Mostrar_categorias(self):
        if(self.conexion.is_connected()):
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM categorias")
                resultados = cursor.fetchall()
                return resultados
            except Error as e:
                print("Error al intentar la conexión: {}".format(e))
    
    def Crear_categoria(self, categoria):
        if(self.conexion.is_connected()):
            try:
                cursor = self.conexion.cursor()
                cursor.execute("INSERT INTO categorias (IDcategoria, NombreCategoria) VALUES ({}, '{}');".format(categoria[0], categoria[1]))
                self.conexion.commit()
                print("Categoria registrada\n")
            except Error as e:
                print("Error al intentar la conexión: {}".format(e))

    def Actualizar_categoria(self, categoria):
        if(self.conexion.is_connected()):
            try:
                cursor = self.conexion.cursor()
                cursor.execute("UPDATE categorias SET NombreCategoria = '{}' WHERE IDcategoria = {};".format(categoria[1], categoria[0]))
                self.conexion.commit()
                print("Categoria actualizada\n")
            except Error as e:
                print("Error al intentar la conexión: {}".format(e))

    def Eliminar_categoria(self, codigoEliminar):
        if(self.conexion.is_connected()):
            try:
                cursor = self.conexion.cursor()
                cursor.execute("DELETE FROM categorias WHERE IDcategoria = {};".format(codigoEliminar))
                self.conexion.commit()
                print("Categoria eliminada\n")
            except Error as e:
                print("Error al intentar la conexión: {}".format(e))
    
    #METODOS DE PRODUCTOS
    def Mostrar_productos(self):
        if(self.conexion.is_connected()):
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT IDproducto, NombreProducto, Precio FROM productos")
                resultados = cursor.fetchall()
                return resultados
            except Error as e:
                print("Error al intentar la conexión: {}".format(e))

    def Crear_producto(self, producto):
        if(self.conexion.is_connected()):
            try:
                cursor = self.conexion.cursor()
                cursor.execute("INSERT INTO productos (IDproducto, NombreProducto, IDcategoria, Precio) VALUES ({}, '{}', {}, '{}');".format(producto[0], producto[1], producto[2], producto[3]))
                self.conexion.commit()
                print("Producto registrado\n")
            except Error as e:
                print("Error al intentar la conexión: {}".format(e))

    def Actualizar_producto(self, producto):
            if(self.conexion.is_connected()):
                try:
                    cursor = self.conexion.cursor()
                    cursor.execute("UPDATE productos SET NombreProducto = '{}', Precio = '{}' WHERE IDproducto = {};".format(producto[1], producto[2], producto[0]))
                    self.conexion.commit()
                    print("Producto actualizado\n")
                except Error as e:
                    print("Error al intentar la conexión: {}".format(e))
    
    def Eliminar_producto(self, codigoEliminar):
        if(self.conexion.is_connected()):
            try:
                cursor = self.conexion.cursor()
                cursor.execute("DELETE FROM productos WHERE IDproducto = {};".format(codigoEliminar))
                self.conexion.commit()
                print("Producto eliminado\n")
            except Error as e:
                print("Error al intentar la conexión: {}".format(e))
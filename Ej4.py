class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Almacen:
    def __init__(self):
        self.productos_recibidos = []
        self.productos_despachar = []

    # A.
    def agregar_producto(self, producto):
        self.productos_recibidos.append(producto)

    # B.
    def despachar_producto(self):
        if self.productos_despachar:
            producto = self.productos_despachar.pop(0)
            print(f'Despachando producto: {producto.nombre} (Cantidad: {producto.cantidad})')
        else:
            print('No hay productos disponibles para despachar.')

    # C.
    def pila_vacia(self):
        return len(self.productos_recibidos) == 0

    # D.
    def cola_vacia(self):
        return len(self.productos_despachar) == 0

    # E.
    def imprimir_productos_recibidos(self):
        print('Lista de productos recibidos:')
        for producto in self.productos_recibidos:
            print(f'Nombre: {producto.nombre} - Cantidad: {producto.cantidad}')

    # F.
    def imprimir_productos_despachar(self):
        print('Lista de productos para despachar:')
        for producto in self.productos_despachar:
            print(f'Nombre: {producto.nombre} - Cantidad: {producto.cantidad}')

    # G.
    def mostrar_cantidad_total_productos(self):
        total = 0
        for producto in self.productos_recibidos:
            total += producto.cantidad
        for producto in self.productos_despachar:
            total += producto.cantidad
        print(f'Cantidad total de productos en el almacén: {total}')

almacen = Almacen()

# A. Agregar productos al almacén (pila).
producto1 = Producto('Pan', 150)
producto2 = Producto('Queso', 75)
producto3 = Producto('Jamón', 60)
producto4 = Producto('Atún', 40)
producto5 = Producto('Energética', 25)

almacen.agregar_producto(producto1)
almacen.agregar_producto(producto2)
almacen.agregar_producto(producto3)
almacen.agregar_producto(producto4)
almacen.agregar_producto(producto5)

# E. Imprimir lista de productos recibidos.
almacen.imprimir_productos_recibidos()

# C. Verificar si la pila de productos recibidos está vacía.
print('¿La pila de productos recibidos está vacía?', almacen.pila_vacia())

# Agregar a la cola 'despachar productos'.
almacen.productos_despachar.append(producto1)
almacen.productos_despachar.append(producto2)
almacen.productos_despachar.append(producto3)
almacen.productos_despachar.append(producto4)
almacen.productos_despachar.append(producto5)

# F. Imprimir lista de productos para despachar.
almacen.imprimir_productos_despachar()

# D. Verificar si la cola de productos para despachar está vacía.
print('¿La cola de productos para despachar está vacía?', almacen.cola_vacia())

# B. Despachar producto.
almacen.despachar_producto()

# G. Mostrar cantidad total de productos en el almacén.
almacen.mostrar_cantidad_total_productos()
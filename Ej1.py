class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None
    
    def agregar_al_final(self, dato):
        nuevonodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevonodo
            self.ultimo = nuevonodo
        else:
            nuevonodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevonodo
            self.ultimo = nuevonodo

    def agregar_al_inicio(self, dato):
        nuevonodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevonodo
            self.ultimo = nuevonodo
        else:
            nuevonodo.siguiente = self.primero
            self.primero.anterior = nuevonodo
            self.primero = nuevonodo

    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def obtener_cabecera(self):
        return self.primero.dato if self.primero else None
    
    def obtener_cola(self):
        return self.ultimo.dato if self.ultimo else None
    
    def existe(self, busqueda):
        actual = self.primero
        while actual:
            if actual.dato == busqueda:
                return True
            actual = actual.siguiente
        return False
    
    def eliminar(self, busqueda):
        actual = self.primero
        while actual:
            if actual.dato == busqueda:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior
                break
            actual = actual.siguiente

lista_reproduccion = ListaDoblementeEnlazada()

# Agregar canciones
lista_reproduccion.agregar_al_final('Cancion 1')
lista_reproduccion.agregar_al_final('Cancion 2')
lista_reproduccion.agregar_al_inicio('Cancion 3')

# Imprimir la lista de reproducción
lista_reproduccion.imprimir()

# Obtener la cabecera y la cola
cabecera = lista_reproduccion.obtener_cabecera()
cola = lista_reproduccion.obtener_cola()
print('Primera canción de la playlist:', cabecera)
print('Última canción de la playlist:', cola)

# Verificar si una canción existe
existe_cancion = lista_reproduccion.existe('Cancion 2')
print('¿Existe la canción 2?', existe_cancion)

# Eliminar una canción
lista_reproduccion.eliminar('Cancion 3')

# Imprimir la lista de reproducción actualizada
lista_reproduccion.imprimir()

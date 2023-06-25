import math

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# La clase también tiene métodos de cálculo, por no dejar las funciones sueltas.
class ListaEnlazada:
    def __init__(self):
        self.primero = None

    # E.
    def esta_vacia(self):
        return self.primero is None

    # A.
    def agregar_dato(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # B.
    def calcular_media(self):
        if self.esta_vacia():
            return None

        total = 0
        contador = 0
        actual = self.primero
        while actual:
            total += actual.dato
            contador += 1
            actual = actual.siguiente
        return total / contador

    # C.
    def calcular_desviacion_estandar(self):
        if self.esta_vacia():
            return None

        media = self.calcular_media()
        suma_cuadrados = 0
        contador = 0
        actual = self.primero
        while actual:
            suma_cuadrados += (actual.dato - media) ** 2
            contador += 1
            actual = actual.siguiente
        varianza = suma_cuadrados / contador
        return math.sqrt(varianza)

    # D.
    def imprimir_lista(self):
        if self.esta_vacia():
            print('La lista está vacía.')
            return

        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def eliminar(self, dato):
        if self.esta_vacia():
            return

        if self.primero.dato == dato:
            self.primero = self.primero.siguiente
            return

        actual = self.primero
        while actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                break
            actual = actual.siguiente

    def existe(self, dato):
        actual = self.primero
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

lista = ListaEnlazada()

# Estado actual de la lista.
print('¿La lista está vacía?', lista.esta_vacia())

# A. Agregar elementos a la lista.
lista.agregar_dato(12)
lista.agregar_dato(65)
lista.agregar_dato(91)
lista.agregar_dato(74)

# Estado actual de la lista.
print('Lista:\n', lista.imprimir_lista())

# B. Calcular media de la lista.
print('Media:', lista.calcular_media())

# C. Calcular deviación estándar.
print('Desviación estándar:', lista.calcular_desviacion_estandar())

# Eliminar, por que quiero.
lista.eliminar(65)

# D. Mostrar lista actual.
print('Lista actualizada:\n', lista.imprimir_lista())

# E. Verificar si está vacía.
print('¿La lista está vacía?', lista.esta_vacia())
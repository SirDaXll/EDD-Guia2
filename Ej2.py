class Cliente:
    def __init__(self, ticket, caja):
        self.ticket = ticket
        self.caja = caja

class Nodo:
    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None

class ColaAtencion:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_al_final(self, cliente):
        nuevo_nodo = Nodo(cliente)
        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def atender_siguiente(self):
        if self.esta_vacia():
            print('No hay clientes en la cola.')
            return

        cliente_atendido = self.cabeza.cliente
        if self.cabeza.siguiente == self.cabeza:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente

        return cliente_atendido

    def imprimir(self):
        if self.esta_vacia():
            print('La cola está vacía.')
            return

        actual = self.cabeza
        while True:
            cliente = actual.cliente
            print('Ticket:', cliente.ticket, '- Caja:', cliente.caja)
            actual = actual.siguiente
            if actual == self.cabeza:
                break

cola = ColaAtencion()

print("¿La cola está vacía?", cola.esta_vacia())

cliente1 = Cliente(1, 'Caja 1')
cliente2 = Cliente(2, 'Caja 2')
cliente3 = Cliente(3, 'Caja 3')
cliente4 = Cliente(4, 'Caja 1')

cola.agregar_al_final(cliente1)
cola.agregar_al_final(cliente2)
cola.agregar_al_final(cliente3)
cola.agregar_al_final(cliente4)

print('Cola:\n', cola.imprimir())

print('Cliente atendido:', cola.atender_siguiente().ticket)

print('\nCola actualizada:\n', cola.imprimir())
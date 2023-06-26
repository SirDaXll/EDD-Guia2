# Clase para identificar cada trabajador.
class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

    def eliminar_subordinado(self, empleado):
        if empleado in self.subordinados:
            self.subordinados.remove(empleado)

    def obtener_subordinados(self):
        return self.subordinados

    def obtener_jefe_directo(self):
        return self.jefe_directo

    def establecer_jefe_directo(self, jefe_directo):
        self.jefe_directo = jefe_directo

# Clase para indicar la jerarquia en la empresa, llamando métodos de la clase Empleado.
class JerarquiaEmpresa:
    def __init__(self):
        self.raiz = None

    # A.
    def agregar_empleado(self, nombre, cargo, jefe_directo=None):
        empleado = Empleado(nombre, cargo)
        if self.raiz is None:
            self.raiz = empleado
        else:
            jefe = self.buscar_empleado(jefe_directo)
            if jefe:
                jefe.agregar_subordinado(empleado)
                empleado.establecer_jefe_directo(jefe)

    # B.
    def eliminar_empleado(self, nombre):
        empleado = self.buscar_empleado(nombre)
        if empleado:
            jefe_directo = empleado.obtener_jefe_directo()
            if jefe_directo:
                jefe_directo.eliminar_subordinado(empleado)
                for subordinado in empleado.obtener_subordinados():
                    jefe_directo.agregar_subordinado(subordinado)
                    subordinado.establecer_jefe_directo(jefe_directo)
            else:
                self.raiz = None

    # D.
    def buscar_empleado(self, nombre):
        return self.buscar_empleado_recursivo(self.raiz, nombre)

    def buscar_empleado_recursivo(self, empleado, nombre):
        if empleado.nombre == nombre:
            return empleado
        for subordinado in empleado.obtener_subordinados():
            resultado = self.buscar_empleado_recursivo(subordinado, nombre)
            if resultado:
                return resultado
        return None

    # C.
    def mostrar_jerarquia(self):
        if self.raiz:
            self.mostrar_jerarquia_recursivo(self.raiz, 0)
        else:
            print('No hay empleados en la jerarquía.')

    def mostrar_jerarquia_recursivo(self, empleado, nivel):
        print('  ' * nivel + '- ' + empleado.nombre + ' (' + empleado.cargo + ')')
        for subordinado in empleado.obtener_subordinados():
            self.mostrar_jerarquia_recursivo(subordinado, nivel + 1)

    # E.
    def obtener_jefe_directo(self, nombre):
        empleado = self.buscar_empleado(nombre)
        if empleado:
            jefe_directo = empleado.obtener_jefe_directo()
            if jefe_directo:
                print('Jefe directo de', empleado.nombre + ':', jefe_directo.nombre + ' (' + jefe_directo.cargo + ')')
            else:
                print(empleado.nombre + ' no tiene un jefe directo.')
        else:
            print('No se encontró al empleado', nombre + '.')

empresa = JerarquiaEmpresa()

# A. Agregar empleado según jerarquía.
empresa.agregar_empleado('CEO', 'Chief Executive Officer')
empresa.agregar_empleado('Vice Presidente 1', 'Ventas y Marketing', 'CEO')
empresa.agregar_empleado('Vice Presidente 2', 'Operaciones', 'CEO')
empresa.agregar_empleado('Gerente Ventas', 'Manager', 'Vice Presidente 1')
empresa.agregar_empleado('Gerente Marketing', 'Manager', 'Vice Presidente 1')
empresa.agregar_empleado('Gerente Control de Producción', 'Manager', 'Vice Presidente 2')
empresa.agregar_empleado('Gerente de Operaciones', 'Manager', 'Vice Presidente 2')
empresa.agregar_empleado('Supervisor 1', 'Zona 1', 'Gerente Ventas')
empresa.agregar_empleado('Supervisor 2', 'Zona 2', 'Gerente Ventas')
empresa.agregar_empleado('Supervisor 3', 'Zona 3', 'Gerente de Operaciones')
empresa.agregar_empleado('Supervisor 4', 'Zona 4', 'Gerente de Operaciones')

# C. Mostrar jerarquía completa.
print('Jerarquía de la empresa:')
empresa.mostrar_jerarquia()

# D. Buscar empleado y mostrar su cargo y subordinados
print('\nBuscar empleado:')
empleado = empresa.buscar_empleado('Gerente Ventas')
if empleado:
    print('Cargo:', empleado.cargo)
    subordinados = empleado.obtener_subordinados()
    if subordinados:
        print('Subordinados:')
        for subordinado in subordinados:
            print(f'- {subordinado.nombre} ({subordinado.cargo})')
    else:
        print('No tiene subordinados.')
else:
    print('Empleado no encontrado.')

# E. Obtener jefe directo de un empleado
print('\nObtener jefe directo:')
empresa.obtener_jefe_directo('Supervisor 2')

# B. Eliminar empleado
empresa.eliminar_empleado('Gerente Ventas')

# C. Mostrar jerarquía actualizada.
print('\nJerarquía de la empresa (actualizada):')
empresa.mostrar_jerarquia()
class Nodo:
    def __init__(self, contenido):
        self.contenido = contenido
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def agg_final(self, contenido):
        nuevo_nodo = Nodo(contenido)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño += 1

    def agg_inicio(self, contenido):
        nuevo_nodo = Nodo(contenido)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamaño += 1

    def agg_posicion(self, contenido, posicion):
        if posicion < 0 or posicion > self.tamaño:
            print("Posición inválida")
            return

        if posicion == 0:
            self.agg_inicio(contenido)
        elif posicion == self.tamaño:
            self.agg_final(contenido)
        else:
            nuevo_nodo = Nodo(contenido)
            actual = self.cabeza
            for _ in range(posicion - 1):
                actual = actual.siguiente
            
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            
            if actual.siguiente is not None:
                actual.siguiente.anterior = nuevo_nodo
            
            actual.siguiente = nuevo_nodo
            self.tamaño += 1

    def imprimir(self):
        nodo = self.cabeza
        while nodo is not None:
            print(nodo.contenido)
            nodo = nodo.siguiente

    def invertir(self):
        nodo = self.cola
        while nodo is not None:
            print(nodo.contenido)
            nodo = nodo.anterior

    def eliminar_duplicado(self):
        if self.cabeza is None:
            return "Lista vacía"

        actual = self.cabeza
        valores_vistos = set()

        while actual is not None:
            if actual.contenido in valores_vistos:
                
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:  
                    self.cabeza = actual.siguiente
                if actual == self.cola:  
                    self.cola = actual.anterior
                self.tamaño -= 1
            else:
                valores_vistos.add(actual.contenido)
            actual = actual.siguiente

    def buscar(self, valor):
        actual = self.cabeza
        posicion = 0

        while actual is not None:
            if actual.contenido == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1

        return -1  

# prueba
lista = ListaDoblementeEnlazada()
lista.agg_final(1)
lista.agg_final(2)
lista.agg_final(5)
lista.agg_final(4)
lista.agg_final(5)

print("Lista antes de eliminar duplicados:")
lista.imprimir()

lista.eliminar_duplicado()
print("Lista después de eliminar duplicados:")
lista.imprimir()

pos = lista.buscar(2)
print(f'Posición de 2: {pos}')

# Agregar un elemento en una posición específica
lista.agg_posicion(3, 2)
print("Lista después de agregar 3 en la posición 2:")
lista.imprimir()

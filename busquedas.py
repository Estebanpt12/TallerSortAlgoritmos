import math

class SearchingAlgorithms:

    @staticmethod
    def busqueda_lineal(lista, objetivo):
        for i in range(len(lista)):
            if lista[i] == objetivo:
                return i 
        return -1  


    @staticmethod
    def lineal_limites_iterativa(arreglo, dato):
        resultado = False
        i = 0
        while i < len(arreglo) and not resultado:
            if arreglo[i] == dato:
                resultado = True
                return resultado
            i += 1
        return resultado


    @staticmethod
    def busqueda_binaria(lista, objetivo):
        inicio = 0
        fin = len(lista) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if lista[medio] == objetivo:
                return medio
            elif lista[medio] < objetivo:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1


    @staticmethod
    def busqueda_por_saltos(lista, objetivo):
        n = len(lista)
        salto = int(math.sqrt(n))
        prev = 0
        while lista[min(salto, n) - 1] < objetivo:
            prev = salto
            salto += int(math.sqrt(n))
            if prev >= n:
                return -1
        for i in range(prev, min(salto, n)):
            if lista[i] == objetivo:
                return i
        return -1 


import time
import matplotlib.pyplot as plt
from busquedas import SearchingAlgorithms
from sorts import SortingAlgorithms  # Importar tus algoritmos

def medir_tiempos_de_sorts(arr):
    # Crear una lista para almacenar los tiempos
    tiempos = []

    # Medir tiempo de Bubble Sort
    medir_tiempo('Bubble Sort', SortingAlgorithms.bubble_sort, arr, tiempos)

    # Medir tiempo de Quicksort
    medir_tiempo('Quicksort', SortingAlgorithms.quicksort, arr, tiempos)

    # Medir tiempo de Stooge Sort
    medir_tiempo('Stooge Sort', SortingAlgorithms.stooge_sort, arr, tiempos)

    # Medir tiempo de Pigeonhole Sort
    medir_tiempo('Pigeonhole Sort', SortingAlgorithms.pigeonhole_sort, arr, tiempos)

    # Medir tiempo de Merge Sort
    medir_tiempo('Merge Sort', SortingAlgorithms.merge_sort, arr, tiempos)

    # Medir tiempo de Bitonic Sort
    medir_tiempo('Bitonic Sort', SortingAlgorithms.bitonic_sort, arr, tiempos)

    # Ordenar los tiempos de mayor a menor
    tiempos.sort(key=lambda x: x[1], reverse=False)

    # Imprimir los tiempos
    for nombre, tiempo in tiempos:
        print(f"{nombre}: {tiempo:.6f} segundos")

    tiempos.sort(key=lambda x: x[1], reverse=True)

    # Graficar los tiempos
    graficar_tiempos(tiempos, "Orednamiento")

def medir_tiempo_busquedas(arr):
    tiempos_busquedas = []
    n = 1250

    #Medir tiempo de busqueda lineal
    medir_tiempo_b('Lineal', SearchingAlgorithms.busqueda_lineal, 
                   arr, tiempos_busquedas, n)

    #Medir tiempo de busqueda lineal limitada
    medir_tiempo_b('Lineal Limitada', SearchingAlgorithms.lineal_limites_iterativa, 
                   arr, tiempos_busquedas, n)

    #Medir tiempo de busqueda binaria
    medir_tiempo_b('Binaria', SearchingAlgorithms.busqueda_binaria, 
                   arr, tiempos_busquedas, n)

    #Medir tiempo de busqueda por saltos
    medir_tiempo_b('Por Saltos', SearchingAlgorithms.busqueda_por_saltos, 
                   arr, tiempos_busquedas, n)

    #Ordenar los tiempos de menor a mayor
    tiempos_busquedas.sort(key=lambda x: x[1])
    print('\n\tTiempos ordenados:')

    #Imprimir los tiempos
    for nombre, tiempo in tiempos_busquedas:
        print(f"{nombre}: {tiempo:.6f} segundos")

    tiempos_busquedas.sort(key=lambda x: x[1], reverse=True)

    # Graficar los tiempos
    graficar_tiempos(tiempos_busquedas, "Busqueda")

def medir_tiempo_b(nombre, funcion, arr, tiempos, n):
    inicio = time.time()
    funcion(arr.copy(), n)
    fin = time.time()
    tiempos.append((nombre, fin - inicio))
    print(f'{nombre} terminado')

def medir_tiempo(nombre, funcion, arr, tiempos):
    inicio = time.time()
    funcion(arr.copy())
    fin = time.time()
    tiempos.append((nombre, fin - inicio))
    print(f'{nombre} terminado')

def graficar_tiempos(tiempos, nombre):
    # Extraer los nombres y los tiempos
    nombres = [nombre for nombre, tiempo in tiempos]
    valores = [tiempo for nombre, tiempo in tiempos]

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.barh(nombres, valores, color='skyblue')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel(f'Algoritmos de {nombre}')
    plt.title('Tiempos de ejecución (orden descendente)')
    plt.gca().invert_yaxis()  # Invertir el eje para que el más lento esté en la parte superior
    plt.show()

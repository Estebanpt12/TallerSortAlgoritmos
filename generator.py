import random

def guardar_arreglo_en_archivo_optimizado(n, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(f"{random.randint(10000000, 99999999)}\n" for _ in range(n))

n = 10000
guardar_arreglo_en_archivo_optimizado(n, "numeros_aleatorios_optimizado_10_000.txt")

n = 100000
guardar_arreglo_en_archivo_optimizado(n, "numeros_aleatorios_optimizado_100_000.txt")

n = 1000000
guardar_arreglo_en_archivo_optimizado(n, "numeros_aleatorios_optimizado_1_000_000.txt")
def leer_arreglo_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        arreglo = [int(linea.strip()) for linea in archivo]
    return arreglo
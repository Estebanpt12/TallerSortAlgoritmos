from lector import leer_arreglo_desde_archivo
import medicion

print('\tTiempos para 10.000')
arr = leer_arreglo_desde_archivo("numeros_aleatorios_optimizado_10_000.txt")
print('Arreglo cargado')
#medicion.medir_tiempos_de_sorts(arr)
medicion.medir_tiempo_busquedas(arr)
print()

print('\tTiempos para 100.000')
arr = leer_arreglo_desde_archivo("numeros_aleatorios_optimizado_100_000.txt")
print('Arreglo cargado')
#medicion.medir_tiempos_de_sorts(arr)
medicion.medir_tiempo_busquedas(arr)
print()

print('\tTiempos para 1.000.000')
arr = leer_arreglo_desde_archivo("numeros_aleatorios_optimizado_1_000_000.txt")
print('Arreglo cargado')
#medicion.medir_tiempos_de_sorts(arr)
medicion.medir_tiempo_busquedas(arr)
print()


import random
import timeit
from merge_sort import merge_sort 
from binary_tree_sort import binary_tree_sort

def generate_data(n):
    return [random.randint(1, 100000) for _ in range(n)]

def measure_execution_time():
    n = 20000
    data = generate_data(n)
    print(f"Cantidad de datos : {n}")
    # Ejecutar y medir Merge Sort
    data_copy = data[:]
    merge_sort_time = timeit.timeit(lambda: merge_sort(data_copy), number=1)
    print(f"Tiempo de ejecución de Merge Sort: {merge_sort_time:.5f} segundos")
    
    # Ejecutar y medir Binary Tree Sort
    data_copy = data[:] 
    binary_tree_sort_time = timeit.timeit(lambda: binary_tree_sort(data_copy), number=1)
    print(f"Tiempo de ejecución de Binary Tree Sort: {binary_tree_sort_time:.5f} segundos")


measure_execution_time()
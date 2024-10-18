import unittest
import random
import time
import psutil
import os
from lab2.task1.src.merge_sort import merge_sort
from lab2.task2.src.number_of_inversions import merge_sort_and_count
from lab2.task3.src.element_of_majority import element_of_majority


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024
    # Возвращает использование памяти в мегабайтах


class AlgorithmsSortTestCase(unittest.TestCase):

    def test1_merge_sort(self):
        A = [random.randint(10**8, 10**9) for _ in range(20000)]
        A_reverse_sort = sorted(A, reverse=True)
        n = len(A)
        start_time = time.perf_counter()
        start_memory = get_memory_usage()

        result = merge_sort(A_reverse_sort, n)

        end_time = time.perf_counter()
        end_memory = get_memory_usage()
        elapsed_time = end_time - start_time
        memory_used = end_memory - start_memory
        print(f"\nВремя работы алгоритма_1: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        (self.assertEqual(result, sorted(A)))

    def test2_inversion_count(self):
        A = [5, 3, 2, 4, 1]  # не отсортированный массив, в котором 8 инверсий!!!
        n = len(A)  # кол-во элементов массива А
        start_time = time.perf_counter()
        start_memory = get_memory_usage()

        result = merge_sort_and_count(A, n)

        end_time = time.perf_counter()
        end_memory = get_memory_usage()
        elapsed_time = end_time - start_time
        memory_used = end_memory - start_memory
        print(f"\nВремя работы алгоритма_2: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        (self.assertEqual(result, 8))

    def test3_1_majority_element(self):
        A = [1]*10000 + [2]*5000 + [3]*4000  # массив, где 1 явлется элементом большинства
        start_time = time.perf_counter()
        start_memory = get_memory_usage()

        result = element_of_majority(A)

        end_time = time.perf_counter()
        end_memory = get_memory_usage()
        elapsed_time = end_time - start_time
        memory_used = end_memory - start_memory
        print(f"\nВремя работы алгоритма_2: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        (self.assertEqual(result, 1))

    def test3_2_majority_element(self):
        A = [1]*5000 + [2]*5000 + [3]*5000  # массив, где нет элемента, который встречается более половины раз
        start_time = time.perf_counter()
        start_memory = get_memory_usage()

        result = element_of_majority(A)

        end_time = time.perf_counter()
        end_memory = get_memory_usage()
        elapsed_time = end_time - start_time
        memory_used = end_memory - start_memory
        print(f"\nВремя работы алгоритма_2: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        (self.assertEqual(result, 0))








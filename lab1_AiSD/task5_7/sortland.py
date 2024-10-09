import tracemalloc
import time
import random

random_numbers = [random.uniform(0, 1000000) for _ in range(3, 10000)]
lines = [f'{len(random_numbers)}\n', ' '.join(map(str, random_numbers))]
file = open('input.txt', 'w')
file.writelines(lines)

tracemalloc.start()
t1 = time.time()

file = open('input.txt', 'r')
n = int(file.readline())
M2 = list(map(float, file.readline().split())) # сортируемый массив
M = [] # исходный неотсортированный массив
S = [] # список с индексами жителей
if (3 <= n <= 9999) and (n % 2 != 0):
    if any(int(m) > 10**6 for m in M):
        print("Элементы массива M не должны превышать значение 10**6!")
    else:
        M = M2
        M2 = sorted(M2)
        minimum = min(M)
        medium = M[n // 2]
        maximum = max(M)
        S = [M2.index(minimum) + 1, M2.index(medium) + 1, M2.index(maximum) + 1]
else:
    print("Количество элементов n должно быть 3 <= n <= 9999, а также n - чётное!")

outfile = open('output.txt', 'w').write(' '.join(map(str, S)))

t2 = time.time()
print("Время работы %s секунд" %(t2-t1))

snapshot = tracemalloc.take_snapshot()
tracemalloc.stop()
top_stats = snapshot.statistics('lineno')
stat = top_stats[0]
print(f"Максимальное использование памяти: {stat.size / 1024:.2f} KB")
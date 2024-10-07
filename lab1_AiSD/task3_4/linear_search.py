import tracemalloc
import time
tracemalloc.start()
t1 = time.time()

file = open('input.txt', 'r')
A = list(map(int, file.readline().split()))
V = int(file.readline())
index = []  # список для подсчета индексов, если элемент встречается несколько раз
print(A)
print(V)
if 0 <= len(A) <= 10**3:
    if any(abs(int(m)) > 10**3 for m in A) or abs(V) >= 10**3:
        print("Введите корректные данные")
    else:
        for i in range(0, len(A)):
            if A[i] == V:
                index.append(i + 1)
            else:
                continue
        if len(index) == 0:
            outfile = open('output.txt', 'w').write('-1 --> Число не найдено!')
        else:
            lines = [f'Число V встречается {len(index)} раз/раза\n',
                     f'Индексы числа V в последовательности: {', '.join(map(str, index))}']
            outfile = open('output.txt', 'w')
            outfile.writelines(lines)
else:
    print("Количество элементов привышает ")

t2 = time.time()
print("Время работы %s секунд" %(t2-t1))

snapshot = tracemalloc.take_snapshot()
tracemalloc.stop()
top_stats = snapshot.statistics('lineno')
stat = top_stats[0]
print(f"Максимальное использование памяти: {stat.size / 1024:.2f} KB")
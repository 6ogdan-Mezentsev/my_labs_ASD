import tracemalloc
import time
import random

random_numbers = [random.randint(0, 1000000000) for _ in range(1000)]
lines = [f'{len(random_numbers)}\n', ' '.join(map(str, random_numbers))]
file = open('../txtf/input.txt', 'w')
file.writelines(lines)

tracemalloc.start()
t1 = time.time()

file = open('../txtf/input.txt', 'r')
n = int(file.readline())
S = list(map(int, file.readline().split()))
if 1 <= n <= 10**3:
    if any(abs(int(m)) > 10**9 for m in S):
        print("Введите корректные данные")
    else:
        for i in range(1, len(S)):
            for j in range(i, 0, -1):
                if S[j] > S[j - 1]:
                    S[j], S[j - 1] = S[j - 1], S[j]
                else:
                    break
else:
    print('Количество элементов должно быть больше чем 1 и меньше чем 10**3')

outfile = open('../txtf/output.txt', 'w').write(' '.join(map(str, S)))

t2 = time.time()
print("Время работы %s секунд" %(t2-t1))

snapshot = tracemalloc.take_snapshot()
tracemalloc.stop()
top_stats = snapshot.statistics('lineno')
stat = top_stats[0]
print(f"Максимальное использование памяти: {stat.size / 1024:.2f} KB")
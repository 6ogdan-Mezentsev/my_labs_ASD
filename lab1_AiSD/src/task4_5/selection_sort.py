import tracemalloc
import time
import random

random_numbers = [random.randint(0, 1000000000) for _ in range(1000)]
lines = [f'{len(random_numbers)}\n', ' '.join(map(str, random_numbers))]
file = open('input.txt', 'w')
file.writelines(lines)

tracemalloc.start()
t1 = time.time()

file = open('input.txt', 'r')
n = int(file.readline())
S = list(map(int, file.readline().split()))
if 1 <= n <= 10**3:
    if any(abs(int(m)) > 10**9 for m in S):
        print("Введите корректные данные")
    else:
        for i in range(0, len(S) - 1):
            M = S[i]
            p = i
            for j in range(i+1, len(S)):
                if M > S[j]:
                    M = S[j]
                    p = j

            if p != i:
                k = S[i]
                S[i] = S[p]
                S[p] = k

else:
    print('Количество элементов должно быть больше чем 1 и меньше чем 10**3')

outfile = open('output.txt', 'w').write(' '.join(map(str, S)))

t2 = time.time()
print("Время работы %s секунд" %(t2-t1))

snapshot = tracemalloc.take_snapshot()
tracemalloc.stop()
top_stats = snapshot.statistics('lineno')
stat = top_stats[0]
print(f"Максимальное использование памяти: {stat.size / 1024:.2f} KB")
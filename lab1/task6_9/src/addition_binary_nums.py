import tracemalloc
import time
tracemalloc.start()
t1 = time.time()

file = open('../txtf/input.txt', 'r')
S = list(map(str, file.readline().split()))
summa = 0
if any(len(i) > 10**3 for i in S):
    if any(len(i) < 1 for i in S):
        print("Количество бит не должно превышать значения 10**3")
else:
    for i in S:
        m = int(i, 2)
        summa += m

outfile = open('../txtf/output.txt', 'w').write(bin(summa)[2:])

t2 = time.time()
print("Время работы %s секунд" %(t2-t1))

snapshot = tracemalloc.take_snapshot()
tracemalloc.stop()
top_stats = snapshot.statistics('lineno')
stat = top_stats[0]
print(f"Максимальное использование памяти: {stat.size / 1024:.2f} KB")

def fib1():
    with open('/Users/6ogdanmezentsev/PycharmProjects/ITMO_project/lab0_АиСД/task3/input.txt', 'r') as file:
        n = int(file.readline())
        file.close()

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    with open('/Users/6ogdanmezentsev/PycharmProjects/ITMO_project/lab0_АиСД/task3/output.txt', 'w') as file:
        file.write(str(a))
        file.close()

fib1()




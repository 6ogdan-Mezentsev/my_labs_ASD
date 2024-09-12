def fib1():
    with open('/Users/6ogdanmezentsev/PycharmProjects/ITMO_project/my_labs_ASD/lab0_АиСД/task2/input.txt', 'r') as file:
        n = int(file.readline())
        file.close()

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    with open('/Users/6ogdanmezentsev/PycharmProjects/ITMO_project/my_labs_ASD/lab0_АиСД/task2/output.txt', 'w') as file:
        file.write(str(a))
        file.close()

fib1()




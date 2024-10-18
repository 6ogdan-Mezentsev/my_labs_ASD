def fib1():
    with open('/my_labs_ASD/lab0/task2_3/input1.txt', 'r') as file:
        n = int(file.readline())
        file.close()
    if 0 <= n <= 45:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b

        with open('/my_labs_ASD/lab0/task2_3/output1.txt', 'w') as file:
            file.write(str(a))
            file.close()
    else:
        print("Введите число корректно!")

fib1()




def fib2():
    with open('/my_labs_ASD/lab0_AiSD/task3/input2.txt', 'r') as file:
        n = int(file.readline())
        file.close()
    if 0 <= n <= 45:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b

        with open('/my_labs_ASD/lab0_AiSD/task3/output2.txt', 'w') as file:
            file.write(str(a % 10))
            file.close()
    else:
        print("Введите число корректно!")

fib2()
import time
from my_labs_ASD.lab0_АиСД.task2.fib1 import fib1
from my_labs_ASD.lab0_АиСД.task3.fib2 import fib2

start_time = time.time()
fib1()
print("Время работы: %s секунд " % (time.time() - start_time))

start_time = time.time()
fib2()
print("Время работы: %s секунд " % (time.time() - start_time))
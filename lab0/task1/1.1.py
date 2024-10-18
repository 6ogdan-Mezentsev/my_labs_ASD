nums = list(map(int, input("Введите два числа через пробел: ").split()))
while not ((-10**9 <= nums[0] <= 10**9) and (-10**9 <= nums[1] <= 10**9)):
    print("Введите число правильно!")
    nums = list(map(int, input("Введите два числа через пробел: ").split()))
print(nums[0] + nums[1])
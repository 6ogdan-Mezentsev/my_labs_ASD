nums = list(map(int, input("Введите два числа через пробел: ").split()))
if (-10**9 <= nums[0] <= 10**9) and (-10**9 <= nums[1] <= 10**9):
    print(nums[0] + nums[1])
else:
    print("Введите число правильно!")
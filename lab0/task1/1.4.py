with open(r'input.txt') as file:
    nums = list(map(int, file.readline().split()))
if (-10**9 <= nums[0] <= 10**9) and (-10**9 <= nums[1] <= 10**9):
    with open('output.txt', 'w') as file:
        file.write(str(nums[0] + nums[1]**2))
else:
    print("Введите число правильно!")
def binary_search(value, lst):
    left = 0
    right = len(lst) - 1
    mid = len(lst) // 2

    while lst[mid] != value and left <= right:
        if value > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    if left > right:
        return -1
    else:
        return mid


if __name__ == "__main__":
    answer = []
    file = open('../txtf/input.txt', 'r')
    n = int(file.readline())
    A = list(map(int, file.readline().split()))
    k = int(file.readline())
    B = list(map(int, file.readline().split()))
    for i in B:
        answer.append(binary_search(i, A))
    result = ' '.join(map(str, answer))
    if 1 <= n <= 10**5 and all(abs(x) <= 10**9 for x in A):
        if 1 <= k <= 10 ** 5 and all(abs(x) <= 10 ** 9 for x in B):
            outfile = open('../txtf/output.txt', 'w').write(result)
    else:
        outfile = open('../txtf/output.txt', 'w').write("Проверьте корректность введённых данных")






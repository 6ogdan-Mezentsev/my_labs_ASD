def merge_sort(A, n):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        merge_sort(left, n)
        merge_sort(right, n)
        # i - индекс в списке left
        # j - индекс в списке right
        # k - индекс в исходном списке A

        # Проверка, нужно ли объединять массивы в том случае, если массивы отсортированы!
        if left[-1] <= right[0]:
            A[:] = left + right

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

        return A
    else:
        return A


if __name__ == "__main__":
    file = open('../txtf/input.txt', 'r')
    n = int(file.readline())
    A = list(map(int, file.readline().split()))
    if (1 <= n <= 20000) and all(abs(x) <= 10 ** 9 for x in A):
        result = ' '.join(map(str, merge_sort(A, n)))
        outfile = open('../txtf/output.txt', 'w').write(result)
    else:
        outfile = open('../txtf/output.txt', 'w').write("Проверьте корректность введённых данных")


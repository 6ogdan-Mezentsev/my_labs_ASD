# Задание 1
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
        i = j = k = 0
        while i < len(left) and j < len(right): # рекурсивно сравниваем элементы отсортированных массивов и добаляем их в исходныый массив А
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while j < len(right): # если в правом массиве остались элементы, а в левом нет
            A[k] = right[j]
            j += 1
            k += 1

        while i < len(left): # если в левом массиве остались элементы, а в правом нет
            A[k] = left[i]
            i += 1
            k += 1

        return A
    else:
        return A


if __name__ == "__main__":
    file = open('input.txt', 'r')
    n = int(file.readline())
    A = list(map(int, file.readline().split()))
    if (1 <= n <= 20000) and all(abs(x) <= 10 ** 9 for x in A):
        result = ' '.join(map(str, merge_sort(A, n)))
        outfile = open('output.txt', 'w').write(result)
    else:
        outfile = open('output.txt', 'w').write("Проверьте корректность введённых данных")











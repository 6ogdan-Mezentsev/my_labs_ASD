# Задача 5
def element_of_majority(A):
    A.sort()
    element = A[len(A) // 2]  # в отсортированном массиве элемент большинства будет стоять по середине!
    count = A.count(element)
    if count > len(A) // 2:
        return 1
    else:
        return 0


if __name__ == "__main__":
    file = open('input.txt', 'r')
    n = int(file.readline())
    A = list(map(int, file.readline().split()))
    if 1 <= n <= 10**5 and all(abs(x) <= 10**9 for x in A):
        outfile = open('output.txt', 'w').write(str(element_of_majority(A)))
    else:
        outfile = open('output.txt', 'w').write("Проверьте корректность введённых данных")



def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
value = input("Введите значение: ")
list_ = get_matrix(n, m, value)
print(list_)

if n and m <= 0:
    print("Только не ноль.")


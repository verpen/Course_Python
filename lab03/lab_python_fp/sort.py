# Задача 4: Необходимо одной строкой кода вывести на экран массив 2,
# который содержит значения массива 1, отсортированные по модулю в порядке убывания

def sort(x):
    return abs(x)


def main():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

    result = sorted(data, key=sort, reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)


if __name__ == "__main__":
    main()

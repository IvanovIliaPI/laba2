def getNumber():

    for num in range(1, 30, 2):

        yield num

def main():

    numbers = list(getNumber())

    print("Список сгенерированных чисел", numbers)
    print("Первое нечетное число:", numbers[0])
    print("Пятое нечетное число:", numbers[4])
    print("Последнее нечетное число:", numbers[-1])

main()
from random import randint

def searchMultipleNumber():

    while True:

        x = input("Введите цифру X: ")
        if x.isdigit() and int(x) != 0:

            x = int(x)
            break
            print("Введите целое число больше нуля.")

    numbers = [randint(10, 200) for i in range(23)]
    print("Сгенерированные числа:", numbers)

    multiples = list(filter(lambda n: n % x == 0, numbers))
    print(f"Числа, кратные {x}: {multiples}")


searchMultipleNumber()
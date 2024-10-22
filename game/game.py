import random

def gameRound():

    variants = ["камень", "ножницы", "бумага"]
    computerVariant = random.choice(variants)
    userVariant = input("Выберите: камень, ножницы или бумага? ").lower().strip()

    while userVariant not in variants:

        print("Неверный выбор. Попробуйте снова.")
        userVariant = input("Выберите: камень, ножницы или бумага? ").lower().strip()

    print(f"Вы выбрали: {userVariant}")
    print(f"Компьютер выбрал: {computerVariant}")

    if userVariant == computerVariant:

        print("Ничья!")
    elif (userVariant == "камень" and computerVariant == "ножницы") or \
            (userVariant == "ножницы" and computerVariant == "бумага") or \
            (userVariant == "бумага" and computerVariant == "камень"):

        print("Вы победили!")
    else:

        print("Компьютер победил!")


def main():

    while True:

        gameRound()
        repeat = input("Хотите сыграть ещё раз? (да/нет): ").lower().strip()
        if repeat != "да":

            break

main()
from datetime import datetime

def calculateAge():

    while True:

        birth = input('Введите дату рождения (дд/мм/гггг): ')
        try:

            day, month, year = map(int,birth.split("/"))
            birth = datetime(year, month, day)
            break
        except ValueError:

            print("Некорректный ввод. Повторите попытку.")


    today = datetime.now()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    print(f"Ваш возраст: {age} лет")


calculateAge()
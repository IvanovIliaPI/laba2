# Аргументы и параметры функции
# Пример функции с одним аргументом
def example(color):
    if color == "green":
        return "This is tree"
    elif color == "blue":
        return "This is sky"
    else:
        return "I don't know"
what_is_it = example('blue')
print(what_is_it)


# Пример позиционных аргументов
def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}
my_cat = cat('Alise', 'Grey', 9)
print(my_cat)

# Пример аргумент - ключевые слова
def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}
my_cat = cat(color = 'Grey', age = 9, name = 'Alise')
print(my_cat)

# Пример получения/разбиения аргументов – ключевых слов с помощью символа *
def example_args(*args):
    print('Positional argument tuple:', args)
example_args()
example_args(1, 2, 4, 'argument')

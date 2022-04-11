def greet():
    name = input('Как вас зовут? ')
    return f'Приятно познакомиться, {name}'

def type_selection():
    number = int(input('C какими числами вы хотите работать: комплексные (формат 1+1j) - 1 или рациональные - 2 (введите 1 или 2):\n'))
    if not number in [1,2]:
        number = int(input('некорректный выбор: выберетe 1 или 2:\n'))
    return number



x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b

def result():
    if y != 0:
        return x / y
    else:
        return 'ошибка: на ноль делить нельзя!'
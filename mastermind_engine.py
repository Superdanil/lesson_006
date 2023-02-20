from random import sample, randint

computer_number = [] # число, загаданное компьютером в формате списка строк
N = 0 # количество быков
M = 0 # количество коров
def think_number():
    """Функция загадывания четырёхзначного числа компьютером. Первая цифра != 0 - не реализовано!"""
    global computer_number
    computer_number = sample(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'), 4)
    print(computer_number)  # для проверки


def check_number(input_number):
    input_number = list(input_number)[:len(computer_number)]    # обрезаем длину введенного числа до длины загаданного
    global N
    global M
    N = 0
    M = 0
    for i in range(4):
        if input_number[i] == computer_number[i]:
            N += 1
        if input_number[i] in computer_number:
            M += 1
    M = M - N
    return {'bulls': N, 'cows': M}


def is_gameover():
    """Если количество быков равно четырём - игра окончена."""
    return N == 4

def choice_num():
    txt = '''Введите
    для работы с рациональными числами: 1
    для работы с комплексными числами: 2
    для выхода: q'''
    print(txt)
    return input("Ввод: ")


def rat():
    txt = """Введите
    для сложения: 1
    для вычитания: 2
    для умножения: 3
    для обычного деления: 4
    для деления с остатком: 5
    для деления нацело: 6
    для возведения в степень: 7
    для извлечения из квадратного корня: 8
    для выхода: q
    для возврата в предыдущее меню: r"""
    print(txt)
    return input("Ввод: ")


def comp():
    com = """Введите
    для сложения: 1
    для вычитания: 2
    для умножения: 3
    для обычного деления: 4
    для выхода: q
    для возврата в предыдущее меню: r"""
    print(com)
    return input("Ввод: ")


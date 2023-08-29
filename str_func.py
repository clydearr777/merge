"""
Функция, принимающая на вход строку и возвращающая её со всеми заглавными буквами
"""

def title(stroka):
    new_stroka = stroka.title()
    return new_stroka


x = str(input())
y = title(x)
print(y)
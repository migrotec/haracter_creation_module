def special_calculation(a, b):
    return a + b - 2

if __name__ == '__main__':
    print('Модуль запущен')
    print('Проверим работу функции')
    # Запуск функции с разными занчениями
    # и сравнение их с ожидаемым ответом.
    print(5 == special_calculation(2, 5))
    print(5 == special_calculation(2, 2))
    print(4 == special_calculation(3, 3)) 
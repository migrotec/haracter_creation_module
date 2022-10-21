# character_creation_module/main.py
# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().


def attack(char_name: str, char_class: str) -> str:
    """Atakuet."""
    ...


def defence(char_name: str, char_class: str) -> str:
    """Zaschita."""
    ...


def special(char_name: str, char_class: str) -> str:
    """Umenie."""
    ...

def start_training(char_name: str, char_class: str) -> str:
    """Nachalo trenerovki."""
    ...

def choice_char_class() -> str:
    """Vibor slassa"""
    ...

def main() -> None:
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))

from math import sqrt

message = """Добро пожаловать в самую лучшую программу для вычисления
квадратного корня из заданного числа"""
print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        return

    print(f"Мы вычислили квадратный корень из введённого вами \
    числа. Это будет: {CalculateSquareRoot(your_number)}")


print(message)
calc(25.5)


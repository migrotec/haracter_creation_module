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
    """Vibor slassa."""
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

   
print("Loading Colorama")
import colorama
from colorama import Fore, Style

colorama.init()  # Инициализация Colorama
print("Colorama loaded successfully!")
print("Welcome to Weak!")

def rainbow_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    rainbow = ""
    for i, char in enumerate(text):
        rainbow += colors[i % len(colors)] + char
    return rainbow + Style.RESET_ALL  # Сброс стиля после текста

def invite():
    while True:  # Бесконечный цикл
        command = input("root# ")
        if command.lower() == "weak":  # Проверяем, ввел ли пользователь "weak" (без учета регистра)
            print(rainbow_text("So weakly, because it's written on Python!"))  # Радужное сообщение
        elif command.lower() == "exit":  # Проверяем, ввел ли пользователь "exit"
            print("Exiting the program. Goodbye!")
            break  # Выходим из цикла и завершаем программу
        else:
            try:
                # Пытаемся вычислить введенное выражение
                result = eval(command)
                print(result)  # Выводим результат
            except Exception as e:
                print("Invalid command. Please try again.")  # Сообщение об ошибке

invite()

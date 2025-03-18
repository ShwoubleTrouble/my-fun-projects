import os
print("Loading Colorama")
import colorama
from colorama import Fore, Style

colorama.init()  # Инициализация Colorama
print("Colorama loaded successfully!")
print("Welcome to Weak!")
print("OPTIMIZED FOR LINUX")

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
        elif command.lower() == "about":
            print ("Weak - pseudo-OS")
            print ("Inspired by GovnOS")
            print ("Updated 2025-03-18")
        elif command.lower() == "gc16":
            print("You started a GC16 emulator, enter file name to run(if you want you can add arguments)")
            filename = (input(""))
            execution = f"./gc16 {filename}"
            os.system(execution)
        elif command.lower() == "gc24":
            print("You started a GC24 emulator, enter file name to run(if you want you can add arguments)")
            filename = (input(""))
            execution = f"./gc24 {filename}"
            os.system(execution)
        elif command.lower() == "start":
            print ("Enter Python file name")
            filename = (input(""))
            execution = f"python3 {filename}"
            os.system(execution)
        elif command.lower() == "help":
            print ("about, 1+1, start, gc24, gc16, exit, weak")
        else:
            try:
                # Пытаемся вычислить введенное выражение
                result = eval(command)
                print(result)  # Выводим результат
            except Exception as e:
                print("Invalid command. Please try again.")  # Сообщение об ошибке

invite()

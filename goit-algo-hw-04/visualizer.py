import sys 
from pathlib import Path 
from colorama import Fore, Style, init 

# Инициализация colorama с автоматическим сбросом стилей
init(autoreset=True)

def visualize_directory_structure(directory: Path, prefix=""):
    if not directory.is_dir():
        print(Fore.RED + "Ошибка: Путь не существует ")
        return
    for item in directory.iterdir():
        if item.is_dir():
            print(Fore.BLUE + prefix + str(item.relative_to(directory)) + "/")
            visualize_directory_structure(item, prefix + "  ")
        else:
            print(Fore.GREEN + prefix + str(item.relative_to(directory)))
def main():
    if len(sys.argv) < 2: 
        print(Fore.RED + "Ошибка: Укажите путь к директории.")  
        return
    # Преобразуем путь в объект Path
    path = Path(sys.argv[1]) 
    # Визуализируем структуру директории (первый вызов функции)
    visualize_directory_structure(path)
    
 # Проверка, запущен ли скрипт как основной модуль   
if __name__=="__main__":
    main()

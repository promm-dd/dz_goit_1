
                
def parse_input(user_input):
    cmd, *args = user_input.split()  #разбивает ввод пользователя на отдельные слова. Первое слово сохраняется как команда cmd, а оставшиеся слова сохраняются в список args с помощью оператора *.
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return  "invalid input use: add "
    name, phone = args
    contacts[name] = phone 
    return f"contact {name} added"

def change_contact(args, contacts):
    if len(args) != 2:
        return "invalid input use: change"
    name, phone = args
    if name in contacts:
        contacts[name] = phone 
        return f"contact {name} updated"
    else:
        return f"contact {name} not found"
    
def get_phone(args, contacts):
    name = args[0]
    return contacts.get(name, f"contact{name} not found")

def all_contacts(contacts):
    if contacts:
        return "\n".join(f"{name} {phone} " for name, phone in contacts.items() )
    else:
        return ("no contacts")
        
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("enter command: ")
        command, args = parse_input(user_input)
        
        if command == "close" or command == "exit":
            print("Good bye")
            break 
        elif command == "hello":
            print("how can i help you")
        elif command == "add":
            print(add_contact(args, contacts))            
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print("invalid command")
            
if __name__ == "__main__":
    main()           

    
    
                
                
                
                
                
                
                
                # contacts ={}
# #функц для добавл контактов 
# def add_contacts(name, phone):
#     contacts[name] = phone 
#     print("контак добавлен")
    
# #функц для измен номера телефона
# def change_contact(name, phone):
#     if name in contacts:
#         contacts[name] = phone 
#         print("контакт обновлен ")
#     else:
#         print("контакт не найден")
        
# #функц для вывода номера телефона по имени 
# def show_phone(name):
#     if name in contacts:
#         print(f"номер тел {name}: {contacts[name]}")
#     else:
#         print("контакт не найден")
    
# #функц для вывода всех контактов 
# def show_all():
#     if contacts:
#         for name, phone in contacts.items():
#             print(f"{name}, {phone}")
#         else:
#             print("нет контактов ")
# #основной цикл бота 
# def main():
#     print("Добро пожаловать в бот")
#     while True:
#         command = input("  введите команду: ").strip().lower()
#         #завершение бота
#         if command in ["close","exit"]:
#             print("Пока")
#             break 
#         #приветствие 
#         elif command == "hello":
#             print("чем могу помочь?  ")
#         # добавление контакта 
#         elif command.startswith("add"):
#             try:
#                 _, name, phone =command.split(" ")
#                 add_contacts(name, phone)
#             except ValueError:
#                 print("неправ формат команды исопольз add:")
#         #изменен контакта 
#         elif command.startswith("change"):
#             try:
#                 _, name, phone = command.split(" ")
#                 change_contact(name, phone)
#             except ValueError: 
#                 print("неправ формат команды исопольз change:")
#         #показ номера по имени 
#         elif command.startswith("phone"):
#             try:
#                  _, name, phone = command.split(" ")
#                  show_phone(name)
#             except ValueError:
#                 print("неправ формат команды исопольз phone:")
#         #команда показа всех контактов 
#         elif command== "all":
#             show_all()
            
#         else:
#             print("неправ команда")
# if __name__ == "__main__":
#     main()
                
                
from random import randrange

min_value= 1
max_value= 1000
quantity = 1000 #это значение указывает сколько уникальных случайных чисел ты хочешь сгенерировать и сохранить в result_array

def get_numbers_ticket(min_value, max_value, quantity):
    # Проверка валидности входных данных
    if min_value <1 or max_value > 1000 or quantity > (max_value - min_value + 1):   #Эта проверка смотрит, не пытаешься ли ты запросить больше уникальных чисел, чем доступно в диапазоне
        return []  # Возвращаем пустой список, если параметры неверные
    
    
    result_array = set()
    while len(result_array) < quantity:
        result_array.add(randrange(min_value, max_value+1))
    return (sorted(list(result_array)))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

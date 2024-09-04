

def total_salary(path): 
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary=0
            count=0 
            for line in file: 
                name, salary =line.split(',')
                salary = int(salary)
                total_salary += salary
                count +=1 
                
            
            average_salary= total_salary/count 
            return total_salary, average_salary
            
    
    except FileNotFoundError: 
        print(f'Error: file {path} not found')
        return None, None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None, None
        
        
total, average = total_salary("/Users/dmitriidridze/dz_goit_1/goit-algo-hw-04/salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

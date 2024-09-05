

def get_cats_info(path):
    try:
        with open(path,'r',encoding='utf-8')as file:
            cats_list= []
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(',')
                cat_info= {
                    'id': cat_id,
                    'name': cat_name,
                    'age': cat_age
                }
                cats_list.append(cat_info)
            
            return cats_list
                
    except FileNotFoundError:
        print(f'Error: file {path} not found')
        return None 
    
    
    
cats_info = get_cats_info("/Users/dmitriidridze/dz_goit_1/goit-algo-hw-04/cats_inf.txt")
print(cats_info)

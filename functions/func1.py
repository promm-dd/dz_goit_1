from datetime import datetime

def get_days_from_today(date):
    try: 
        input_date= datetime.strptime(date.strip(), "%Y-%m-%d").date()
    except ValueError:
        return "invalid date. Use 'YYYY-MM-DD' "
    current_date= datetime.today().date()
    delta= current_date - input_date
    return delta.days

date_string = "2023-12-05"
days_difference =get_days_from_today(date_string)
print(days_difference)

get_days_from_today("2021-10-09")


date_string_invalid = "2021.10.09"
days_invalid = get_days_from_today(date_string_invalid)
print(days_invalid)
from datetime import datetime

def get_days_from_today(date):
    input_date= datetime.strptime(date.strip(), "%Y-%m-%d").date()
    current_date= datetime.today().date()
    delta= current_date - input_date
    return delta.days

date_string = "2023-12-05"
days_difference =get_days_from_today(date_string)
print(days_difference)
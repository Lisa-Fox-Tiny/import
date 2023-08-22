from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    print(f'Сегодня: {datetime.today().strftime("%d-%m-%Y %H:%M")}')
    calculate_salary()
    get_employees()
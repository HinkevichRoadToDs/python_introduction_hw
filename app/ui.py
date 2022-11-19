from csv_module import fieldnames
def get_mode():
    mode = int(input('Введите действие, которое вы хотите совершить:\n'
                     '1 - найти запись в БД\n'
                     '2 - посмотреть структуру БД\n'
                     '3 - добавить запись в БД\n'
                     '4 - удалить запись из БД\n'
                     '5 - изменить существующую запись : '))
    return mode
def get_parameter():
    param_dict = {}
    print('по каким атрибутам вы будете фильтровать?\n'
          '1 - id\n'
          '2 - name\n'
          '3 - surname\n'
          '4 - email\n'
          '5 - salary : ')
    for i in range(4):
        param = input('Введите номер атрибута или точку, чтобы закончить: ')
        if param != '.':
            param_dict[fieldnames[int(param)-1]] = input('Введите значение для поиска: ')
        else:
            break
    return param_dict

def display_filtered_data(data):
    print('Результат поиска:\n', data)




import datetime as dt


def create_log(action, searching=None, row_numb=None, changes=None):
    time = dt.datetime.now().strftime('%H:%M:%S')
    with open('app/data/logs.csv', 'a') as log_file:
        log_file.write(f'{time};{action};{searching};{row_numb};{changes}\n')

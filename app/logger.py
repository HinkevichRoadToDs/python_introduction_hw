import pathlib as pl
from datetime import datetime as dt


def do_log(vars, mode, res):
    str_vars = []
    for item in vars:
        str_vars.append(str(item))
    time = dt.now()
    path = pl.Path('app', 'log.csv')
    with open(path, 'a') as log_file:
        log_file.write(f'time:{time};variables:{";".join(str_vars)};mode:{mode};result:{res}\n')

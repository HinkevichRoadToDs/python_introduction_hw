import pandas as pd
from ui import fieldnames
import csv

fieldnames = ['id', 'name', 'surname', 'email', 'salary']


def filter_data(filter_on, args: dict):
    data = pd.read_csv('app/data/data.csv', sep=',')
    if filter_on:
        query = ""
        for key, value in args.items():
            if key == 'id':
                query += f"{value} == `id` and "
            if key == 'name':
                query += f"'{value}' in `name` and "
            if key == 'surname':
                query += f"'{value}' in `surname` and "
            if key == 'email':
                query += f"'{value}' in `email` and "
        query = query[:-5]
        return data.query(query)
    else:
        return data


def append_data(dict_new):
    with open('app/data/data.csv', 'a', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        max_id = 1
        for row in csv_writer:
            if max_id < int(row['id']):
                max_id = int(row['id'])
        csv_writer.writerow(dict_new)
import pandas as pd
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
    with open('app/data/data.csv', 'r') as file:
        csv_reader = csv.DictReader(file, fieldnames=fieldnames)
        max_id = 1
        for row in csv_reader:
            try:
                if max_id < int(row['id']):
                    max_id = int(row['id'])
            except:
                continue
    new_max_id = max_id + 1
    dict_new['id'] = new_max_id
    with open('app/data/data.csv', 'a', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writerow(dict_new)
    return new_max_id

def change_data(row_numb, changes_dict: dict):
    with open('app/data/data.csv', 'r') as file:
        csv_reader = csv.DictReader(file, fieldnames=fieldnames)
        list_dicts = []
        new_row = {}
        for row in csv_reader:
            try:
                if int(row['id']) == row_numb:
                    new_row = row
                    for key in changes_dict.keys():
                        new_row[key] = changes_dict[key]
                    # print(new_row)
                    list_dicts.append(new_row)
                else:
                    list_dicts.append(row)
            except:
                continue

    with open('app/data/data.csv', 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for item in list_dicts:
            csv_writer.writerow(item)

def remove_data(row_numb):
    with open('app/data/data.csv','r') as file:
        csv_reader = csv.DictReader(file,fieldnames=fieldnames)
        list_dicts = []
        removed_element = 0
        for row in csv_reader:
            try:
                if row_numb == int(row['id']):
                    removed_element = row
                    continue
                else:
                    list_dicts.append(row)
            except:
                continue

    with open('app/data/data.csv', 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for item in list_dicts:
            csv_writer.writerow(item)
    return removed_element
'''
3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''
# сжатие и помещение в файл
with open('file.txt', 'r', encoding='utf-8') as data:
    lst_with_char = []
    for line in data:
        line_lst = []
        for item in line.replace('\n', ''):
            line_lst.append(item)
        lst_with_char.append(line_lst)
    rle_lst = []
    for lst in lst_with_char:
        lst_2 = []
        prev_symbol = lst[0]
        count = 0
        for symbol in lst:
            if symbol != prev_symbol:
                lst_2.append(str(count) + str(prev_symbol))
                count = 1
            else:
                count += 1
            prev_symbol = symbol
        last_char = symbol
        count = 0
        for item in lst[:: -1]:
            if item == last_char:
                count += 1
            else:
                lst_2.append(str(count) + str(last_char))
                break
        rle_lst.append(lst_2)
rle_file = open('rle_file.txt', 'w')
for item in rle_lst:
    rle_file.write(''.join(item) + '\n')
rle_file.close()
# извлечение и раскодирование
with open('rle_file.txt', 'r') as input_data:
    data = input_data.read()
    data = data.splitlines()
    encoded_data = []
    for line in data:
        new_line = ''
        count = ''
        for item in line:
            if item.isdigit():
                count += item
            else:
                new_line += item * int(count)
                count = ''
        encoded_data.append(new_line)
encoded_datafile = open('encoded_datafile.txt','w')
for line in encoded_data:
    encoded_datafile.write(line + '\n')
encoded_datafile.close()

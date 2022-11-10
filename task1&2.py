'''
Дана последовательность чисел. Получить отсортированный по возрастанию список уникальных
элементов заданной последовательности.
Пример:
[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
'''
# num_lst = [1, 2, 3, 5, 1, 5, 3, 10, 32, 12, 9, 333, 333]
# unique_values = []
#
#
# def find_unique(item):
#     if item in unique_values:
#         return False
#     else:
#         unique_values.append(item)
#         return True
#
#
# unique_lst = sorted(list(filter(find_unique, num_lst)))
# print(unique_lst)

'''
Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный.
Пример:
2+2 => 4;
1+2*3 => 7;
1-2*3 => -5;
**Добавьте возможность использования скобок, меняющих приоритет операций.
'''
expr = input('введите выражение(например:22*3+50/(423+20)*20) : ')
splitted_expr = []

def str_to_lst(expression):
    for i in range(len(expression)):
        if not expression[i].isalnum() and expression[i] != '(' and expression[i] != ')':
                splitted_expr.append(expression[:i])
                splitted_expr.append(expression[i])
                print(expression)
                return str_to_lst(expression[i + 1:])
        elif expression[i] == '(':
            splitted_expr.append(expression[i])
            return str_to_lst(expression[i + 1:])
        elif expression[i] == ')':
            splitted_expr.append(expression[:i])
            splitted_expr.append(expression[i])
            try:
                splitted_expr.append(expression[i+1])
                return str_to_lst(expression[i + 2:])
            except:
                return
        if expression.isdigit():
            splitted_expr.append(expression)
            return


str_to_lst(expr)
print(splitted_expr)

def solve_expression(splitted_expression:list):
    while '(' and ')' in splitted_expression:
        lft_idx = splitted_expression.index('(')
        rht_idx = splitted_expression.index(')')
        splitted_expression = splitted_expression[:lft_idx] + do_math(splitted_expression[lft_idx + 1:rht_idx]) + splitted_expression[rht_idx + 1:]
    splitted_expression = do_math(splitted_expression)
    return splitted_expression
def do_math(equation:list):

    while len(equation) != 1:
        for sign in '/*+-':
            while sign in equation:
                idx = equation.index(sign)
                equation = equation[:idx-1] + simple_math(equation[idx-1:idx+2]) + equation[idx+2:]

    return equation

def simple_math(operation:list):
    if operation[1] == '/':
        return [str(float(operation[0]) / float(operation[2]))]
    if operation[1] == '*':
        return [str(float(operation[0]) * float(operation[2]))]
    if operation[1] == '+':
        return [str(float(operation[0]) + float(operation[2]))]
    if operation[1] == '-':
        return [str(float(operation[0]) - float(operation[2]))]


print(f'точный ответ : {float(solve_expression(splitted_expr)[0])}\n'
      f'округленный ответ {round(float(solve_expression(splitted_expr)[0]), 2)}')
print(22*3+50/(423+20)*20)
# def solve_expression(expr_lst):
#     while '(' and ')' in expr_lst:
#         try:
#             lft_bracket_idx = expr_lst.index('(')
#             rht_bracket_idx = expr_lst.index(')')
#             expr_lst = expr_lst[:lft_bracket_idx] + solve_part(expr_lst[lft_bracket_idx + 2:lft_bracket_idx - 1]) + expr_lst[rht_bracket_idx+1:]
#         except:
#             break
#     return expr_lst
# def solve_part(part: list):
#     for sign in '*/+-':
#         while sign in part:
#             idx = part.index(sign)
#             part = part[:idx - 1] + part[idx - 1:idx + 2] + part[idx + 2:]
#     return part
#
#
# def simple_math(operation: list):
#     if operation[1] == '/':
#         return str(float(operation[0]) / float(operation[2]))
#     if operation[1] == '*':
#         return str(float(operation[0]) * float(operation[2]))
#     if operation[1] == '+':
#         return str(float(operation[0]) + float(operation[2]))
#     if operation[1] == '-':
#         return str(float(operation[0]) - float(operation[2]))
#
#
#
# result = solve_expression(splitted_expr)
# print(result)
# print(solve_part(['3', '*', '4']))
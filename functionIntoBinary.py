def binary(number: int) -> str:
    temp = number
    if number < 0:
        number *= -1
    binary_number = ''
    while True:
        if number != 1:
            binary_number += str(number % 2)
            number //= 2
        elif number == 1:
            binary_number += '1'
            binary_number = ''.join(reversed(binary_number))
            break
    if temp < 0:
        neg_binary_number = ''
        for i in binary_number:
            if i == '1':
                neg_binary_number += '0'
            else:
                neg_binary_number += '1'
        binary_number = neg_binary_number[::]
        binary_number = '1' + binary_number
    return binary_number

# def binary(number: int) -> str:
#     bin_num = ''
#     while number > 0:
#         bin_num = str(number % 2) + bin_num
#         number = number // 2
#     return bin_num
#
#
# def return_result(number):
#     if number < 0:
#         number *= -1
#         neg_binary_number = ''
#         binary_number = binary(number)
#         for i in binary_number:
#             if i == '1':
#                 neg_binary_number += '0'
#             else:
#                 neg_binary_number += '1'
#         return neg_binary_number
#     else:
#         return binary(number)
# print(return_result(-110))
from ui import get_args

arguments = []


# def init(arg):
#     global arguments
#     arguments.append(arg)


def full_init():
    while True:
        arg = get_args()
        if arg == '.':
            break
        else:
            if 'j' in arg:
                arg = complex(arg)
                arguments.append(arg)
            else:
                arguments.append(float(arg))
    return arguments


def simple_math(mode):
    result = 0
    if mode == 1:
        for arg in arguments:
            result += arg
        return result
    if mode == 2:
        result = arguments[0]
        arguments.pop(0)
        for arg in arguments:
            result -= arg
        return result
    if mode == 3:
        result = 1
        for arg in arguments:
            result *= arg
        return result
    if mode == 4:
        result = arguments[0]
        arguments.pop(0)
        for arg in arguments:
            result /= arg
        return result

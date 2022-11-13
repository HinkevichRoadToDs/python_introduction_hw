from model import full_init, simple_math
from ui import get_mode, get_result
from logger import do_log


def start_engine():
    args_log = tuple(full_init())
    mode_log = get_mode()
    result = simple_math(mode_log)
    print(get_result(result))
    do_log(args_log, mode_log, result)

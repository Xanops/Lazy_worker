import concurrent.futures
from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    print(button)

    '''Stop listener'''
    # if not pressed:
    #    return False


def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))


def mouse_listener():
    # Collect events until released
    listener = Listener(  # on_move=on_move,
                             on_click=on_click,
                             on_scroll=on_scroll)
    listener.start()
    listener_disp = concurrent.futures.ThreadPoolExecutor().submit(listener)

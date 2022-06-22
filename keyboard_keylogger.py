from pynput.keyboard import Key, Listener
import threading
import concurrent.futures


def on_press(key):
    print('{0}:{1} pressed'.format(
        key, key.vk if hasattr(key, "vk")
        else ""))

    if hasattr(key, "from_char"):
        if key == key.from_char('Я'):
            print("Вы нажали Я")
        elif key == key.from_char('я'):
            print("Вы нажали я")


def on_release(key):
    print('{0}:{1} released'.format(
        key, key.vk if hasattr(key, "vk")
        else ""))
    # print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        print("Вы завершили прослушивание нажатий")
        raise Exception
        # return False


def keyboard_listener():
    # Collect events until released
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener_disp = concurrent.futures.ThreadPoolExecutor().submit(listener)

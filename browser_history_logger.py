import browser_history


def print_history():
    while True:
        outputs = browser_history.get_history()
        print(outputs.to_csv())

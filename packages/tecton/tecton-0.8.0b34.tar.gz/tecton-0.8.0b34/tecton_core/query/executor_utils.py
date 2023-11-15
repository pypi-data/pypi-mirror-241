import sys
import threading
import time
import typing


def detect_interactive_shell():
    try:
        import IPython
    except ImportError:
        return False

    return IPython.get_ipython() is not None


def display_timer(str_template: str, output: typing.IO = sys.stdout) -> typing.Callable[[], None]:
    timer = 0
    finished = threading.Event()

    def fn():
        nonlocal timer

        while True:
            if finished.is_set():
                return
            minutes = timer // 60
            seconds = timer % 60
            timer += 1
            output.write("\r")
            output.write(str_template.format(clock=f"{minutes:02d}:{seconds:02d}"))
            output.flush()
            time.sleep(1)

    def cancel():
        output.write("\n")
        output.flush()

        finished.set()

    t = threading.Thread(target=fn)
    t.start()
    return cancel

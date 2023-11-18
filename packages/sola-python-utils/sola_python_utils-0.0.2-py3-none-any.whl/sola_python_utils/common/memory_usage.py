import subprocess
import time

from .line_notify import notify


def memory_usage():
    while True:
        args = ["free", "-g"]
        res = subprocess.check_output(args)
        conv = res.decode("utf-8").split()
        string = (
            f"{conv[6]} {conv[8]}/{conv[7]} {int(int(conv[8]) / int(conv[7]) * 100)}%"
        )
        print(string)
        notify(string)
        time.sleep(3)

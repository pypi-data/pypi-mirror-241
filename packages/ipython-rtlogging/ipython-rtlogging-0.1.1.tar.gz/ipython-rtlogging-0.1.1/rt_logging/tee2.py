import sys
import time


class ipythonStream():
    def __init__(self, cell_display):
        self.cell_display = cell_display

        self.ori = sys.stdout

    def __enter__(self):
        sys.stdout = self

    def write(self, msg):
        self.cell_display.update(msg.replace("\n", ""))

    def flush(self):
        time.sleep(1)  # test TODO

    def close(self):
        sys.stdout = self.ori

    def __exit__(self, *args):
        self.close()
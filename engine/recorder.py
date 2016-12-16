import time
from audiostream import get_input


def callback_mic(data):
    print('Received', len(data))


def record():
    mic = get_input(callback=callback_mic)
    mic.start()
    time.sleep(5)
    mic.stop()

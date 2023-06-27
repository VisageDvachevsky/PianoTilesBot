import time
import keyboard

def wait_until_start():
    while True:
        time.sleep(0.05)
        if keyboard.is_pressed('q'):
            time.sleep(0.1)
            break
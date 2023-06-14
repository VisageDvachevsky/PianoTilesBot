import cv2
import numpy as np
import time
import threading
from PIL import ImageGrab
import ctypes
import pyautogui

ZONE_X = 550
ZONE_Y = 170
ZONE_WIDTH = 700
ZONE_HEIGHT = 700

def Move(x, y):
    user32 = ctypes.windll.user32
    user32.SetCursorPos(x, y)

def ClickMouse():
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004

    user32 = ctypes.windll.user32
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def detect_black_tile(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    binary_inverse = cv2.bitwise_not(binary)
    contours, _ = cv2.findContours(binary_inverse, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        return True, contours[0]
    else:
        return False, None

def is_cursor_on_black(x, y):
    screenshot = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
    pixel = screenshot.getpixel((0, 0))
    return pixel == (0, 0, 0)

def tile_detector():
    while not exit_flag.is_set():
        screenshot = ImageGrab.grab()
        image = np.array(screenshot)

        zone_image = image[ZONE_Y:ZONE_Y + ZONE_HEIGHT, ZONE_X:ZONE_X + ZONE_WIDTH]

        is_black_tile, contour = detect_black_tile(zone_image)

        if is_black_tile:
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)

            bottom_y = box[:, 1].max()

            cursor_x = ZONE_X + int(rect[0][0])
            cursor_y = ZONE_Y + int(bottom_y)

            if is_cursor_on_black(cursor_x, cursor_y):
                Move(cursor_x, cursor_y)
                ClickMouse()

exit_flag = threading.Event()
exit_flag.clear()

time.sleep(2)

thread = threading.Thread(target=tile_detector)
thread.start()


 

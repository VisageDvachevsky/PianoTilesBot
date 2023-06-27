import cv2
import numpy as np
import threading
from PIL import ImageGrab
import win32api
import pyautogui

class TileDetector:
    def __init__(self, zone_x, zone_y, zone_width, zone_height):
        self.zone_x = zone_x
        self.zone_y = zone_y
        self.zone_width = zone_width
        self.zone_height = zone_height
        self.cached_screenshot = None
        self.exit_flag = threading.Event()
        self.exit_flag.clear()

    def move(self, x, y):
        win32api.SetCursorPos((x, y))

    def click_mouse(self):
        MOUSEEVENTF_LEFTDOWN = 0x0002
        MOUSEEVENTF_LEFTUP = 0x0004

        win32api.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def detect_black_tile(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        binary_inverse = cv2.bitwise_not(binary)
        contours, _ = cv2.findContours(binary_inverse, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            return True, contours[0]
        else:
            return False, None

    def is_cursor_on_black(self, x, y):
        if self.cached_screenshot is not None:
            pixel = self.cached_screenshot[y - self.zone_y, x - self.zone_x]

        else:
            screenshot = ImageGrab.grab(bbox=(self.zone_x, self.zone_y, self.zone_x + self.zone_width, self.zone_y + self.zone_height))
            pixel = screenshot.getpixel((x, y))
        return np.all(pixel == (0, 0, 0))

    def capture_screenshot(self):
        screenshot = ImageGrab.grab(bbox=(self.zone_x, self.zone_y, self.zone_x + self.zone_width, self.zone_y + self.zone_height))
        self.cached_screenshot = np.array(screenshot)

    def tile_detector(self):
        while not self.exit_flag.is_set():
            image = self.cached_screenshot

            is_black_tile, contour = self.detect_black_tile(image)

            if is_black_tile:
                rect = cv2.minAreaRect(contour)
                box = cv2.boxPoints(rect)
                box = np.int0(box)

                bottom_y = box[:, 1].max()

                cursor_x = self.zone_x + int(rect[0][0])
                cursor_y = self.zone_y + int(bottom_y)

                if self.is_cursor_on_black(cursor_x, cursor_y):
                    self.move(cursor_x, cursor_y)
                    self.click_mouse()

    def start_detection(self):
        screenshot_thread = threading.Thread(target=self.capture_screenshot)
        screenshot_thread.start()

        while not self.exit_flag.is_set():
            self.capture_screenshot()
            image = self.cached_screenshot

            is_black_tile, contour = self.detect_black_tile(image)

            if is_black_tile:
                rect = cv2.minAreaRect(contour)
                box = cv2.boxPoints(rect)
                box = np.int0(box)

                bottom_y = box[:, 1].max()

                cursor_x = self.zone_x + int(rect[0][0])
                cursor_y = self.zone_y + int(bottom_y)

                if self.is_cursor_on_black(cursor_x, cursor_y):
                    self.move(cursor_x, cursor_y)
                    self.click_mouse()

if __name__ == "__main__":
    zone_x = 550
    zone_y = 170
    zone_width = 700
    zone_height = 700

    detector = TileDetector(zone_x, zone_y, zone_width, zone_height)
    detector.start_detection()

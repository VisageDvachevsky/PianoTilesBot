import cv2
import numpy as np
import mss

class Detector:
    ZONE_X = 550
    ZONE_Y = 300
    ZONE_WIDTH = 700
    ZONE_HEIGHT = 600
    CHECK_REGION_SIZE = 70
    SPEED_OFFSET = 100

    def __init__(self):
        self.__sct = mss.mss()
        self.__kernel = np.zeros((self.CHECK_REGION_SIZE, self.CHECK_REGION_SIZE), dtype=np.uint8)
        self.__monitor = {"top": self.ZONE_Y, "left": self.ZONE_X, "width": self.ZONE_WIDTH, "height": self.ZONE_HEIGHT}
        self.__calibration_offset = (self.ZONE_X, self.ZONE_Y + self.SPEED_OFFSET)
        self.__y_range = np.arange(Detector.ZONE_HEIGHT - self.CHECK_REGION_SIZE, 0, -30)
        self.__x_range = np.arange(0, self.ZONE_WIDTH - self.CHECK_REGION_SIZE, 30)

    def __get_black_pos(self, binary, y_range, x_range):
        region_size = self.CHECK_REGION_SIZE
        for y in y_range:
            for x in x_range:
                if np.array_equal(binary[y:y + region_size, x:x + region_size], self.__kernel):
                    return (x + region_size // 2, y + region_size // 2)
        return None

    def __detect_black_tile(self, image):
        binary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(binary, 1, 255, cv2.THRESH_BINARY)
        return self.__get_black_pos(binary, self.__y_range, self.__x_range)

    def __get_screenshot(self):
        screenshot = self.__sct.grab(self.__monitor)
        image = np.array(screenshot)
        return image

    def get_tile_pos(self):
        screenshot = self.__get_screenshot()
        zone_position = self.__detect_black_tile(screenshot)
        if not zone_position:
            return None

        cursor_x = np.add(self.__calibration_offset[0], zone_position[0]).astype(int).item()
        cursor_y = np.add(self.__calibration_offset[1], zone_position[1]).astype(int).item()


        return cursor_x, cursor_y

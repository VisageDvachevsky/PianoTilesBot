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
        self.__sct = mss.mss(with_cursor=False)
        self.__kernel = np.zeros((self.CHECK_REGION_SIZE, self.CHECK_REGION_SIZE))

    def __get_black_pos(self, binary):
        for y in range(self.ZONE_HEIGHT - self.CHECK_REGION_SIZE, 0, -30):
            for x in range(0, self.ZONE_WIDTH - self.CHECK_REGION_SIZE, 30):
                if (binary[y:y + self.CHECK_REGION_SIZE, x:x + self.CHECK_REGION_SIZE] == self.__kernel).all():
                    return (x + self.CHECK_REGION_SIZE // 2, y + self.CHECK_REGION_SIZE // 2)
        return None

    def __detect_black_tile(self, image):
        binary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(binary, 1, 255, cv2.THRESH_BINARY)
        return self.__get_black_pos(binary)


    def __get_screenshot(self):
        screenshot = self.__sct.grab(self.__sct.monitors[1])
        image = np.array(screenshot)
        zone_image = image[self.ZONE_Y:self.ZONE_Y + self.ZONE_HEIGHT,
                           self.ZONE_X:self.ZONE_X + self.ZONE_WIDTH]
        return zone_image

    def get_tile_pos(self):
        screenshot = self.__get_screenshot()
        zone_position = self.__detect_black_tile(screenshot)
        if not zone_position:
            return None

        cursor_x = self.ZONE_X + zone_position[0]
        cursor_y = self.ZONE_Y + zone_position[1] + self.SPEED_OFFSET

        return cursor_x, cursor_y
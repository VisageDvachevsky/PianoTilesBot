import keyboard
from detectors.detector import Detector
from controllers.mouse_controller import MouseController
from utils import wait_until_start

def main():
    detector = Detector()
    mouse_controller = MouseController()

    exit_flag = False
    while not exit_flag:
        pos = detector.get_tile_pos()

        if pos:
            mouse_controller.move(pos[0], pos[1])
            mouse_controller.click()

        if keyboard.is_pressed('q'):
            exit_flag = True

if __name__ == '__main__':
    wait_until_start()
    main()


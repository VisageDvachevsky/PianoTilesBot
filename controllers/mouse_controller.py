import ctypes

class MouseController:
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004

    def move(self, x, y):
        ctypes.windll.user32.SetCursorPos(x, y)

    def click(self):
        ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

import ctypes

class MouseController:
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004

    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.set_cursor_pos = self.user32.SetCursorPos
        self.mouse_event = self.user32.mouse_event

    def move(self, x, y):
        self.set_cursor_pos(x, y)

    def click(self):
        self.mouse_event(self.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        self.mouse_event(self.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

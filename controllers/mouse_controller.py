from win32api import SetCursorPos, mouse_event

class MouseController:
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004

    def move(self, x, y):
        SetCursorPos((x, y))

    def click(self):
        mouse_event(self.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        mouse_event(self.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

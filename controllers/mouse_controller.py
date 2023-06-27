import win32api

class MouseController:
    def move(self, x, y):
        win32api.SetCursorPos((x, y))

    def click(self):
        MOUSEEVENTF_LEFTDOWN = 0x0002
        MOUSEEVENTF_LEFTUP = 0x0004

        win32api.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

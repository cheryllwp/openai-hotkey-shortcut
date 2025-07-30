import ctypes
import time
import win32gui
import win32con

def bring_cmd_to_front():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Restore if minimized
        win32gui.SetForegroundWindow(hwnd)
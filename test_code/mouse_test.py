import time as T

import win32api as win_a
import win32con as win_c


def mouse_click(x, y):
	win_a.SetCursorPos((x, y))
	win_a.mouse_event(win_c.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
	win_a.mouse_event(win_c.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

# print(win_a.GetCursorPos())
# win_a.SetCursorPos(move_pos)

# mouse_click(300, 300)

# win_a.ClipCursor((200, 200, 700, 700))
#
# T.sleep(1)
#
# win_a.ClipCursor((0, 0, 0, 0))


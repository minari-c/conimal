import win32clipboard as win_clip
import win32api as win_a

print('Width: ', win_a.GetSystemMetrics(0))
print('Height: ', win_a.GetSystemMetrics(1))

print(win_a.GetLocalTime())
print(win_a.GetSystemTime())

print(win_a.GetComputerName())
print(win_a.GetUserName())

win_clip.OpenClipboard()
win_clip.EmptyClipboard()
win_clip.SetClipboardText('야옹')
win_clip.CloseClipboard()

win_clip.OpenClipboard()
data = win_clip.GetClipboardData()
win_clip.CloseClipboard()

print(data)

import win32api
import time
import win32con
import win32gui
import re
import sys
import win32clipboard



VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_NEXT_TRACK = 0xB0
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
VK_MEDIA_STOP = 0xB2
results = []
top_windows = []
commands = {'play_pause': VK_MEDIA_PLAY_PAUSE}


VK_CODE = {
'winkey': 0x5B,
'rkey': 0x52,
'enter': 0x0D,
'ctrl': 0x11,
'vkey': 0x56,
'tab': 0x09,
'alt': 0x12
} 

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

           
def pressHoldRelease(*args):
    '''
    press and hold passed in strings. Once held, release
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').

    this is useful for issuing shortcut command or shift commands.
    e.g. pressHoldRelease('ctrl', 'alt', 'del'), pressHoldRelease('shift','a')
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0,0,0)
        time.sleep(.05)
            
    for i in args:
            win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
            time.sleep(.1)

def set_clipboard(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text.encode('utf-8'),
                    win32clipboard.CF_TEXT)
    win32clipboard.SetClipboardText(unicode(text),
                    win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

set_clipboard(sys.argv[1])
hwcode = win32api.MapVirtualKey(commands[play_pause], 0)
win32api.keybd_event(commands[play_pause], hwcode)
pressHoldRelease('winkey', 'rkey')
pressHoldRelease('ctrl', 'vkey')
pressHoldRelease('enter')

time.sleep(1)

win32gui.EnumWindows(windowEnumerationHandler, top_windows)
for i in top_windows:
    if "spotify" == i[1].lower():
        print i
        win32gui.ShowWindow(i[0],5)
        win32gui.SetForegroundWindow(i[0])
        break
time.sleep(1)

pressHoldRelease('tab')
pressHoldRelease('tab')
pressHoldRelease('enter')
#spotify:user:spotify:playlist:0eDq2STmk8tKcD7qWCwrze
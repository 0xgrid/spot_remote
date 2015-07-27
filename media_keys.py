import win32api
import sys

VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_NEXT_TRACK = 0xB0
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
VK_MEDIA_STOP = 0xB2

commands = {'play_pause': VK_MEDIA_PLAY_PAUSE, 'next': VK_MEDIA_NEXT_TRACK, 'vol_up': VK_VOLUME_UP, 'vol_down': VK_VOLUME_DOWN, 'stop': VK_MEDIA_STOP}
hwcode = win32api.MapVirtualKey(commands[sys.argv[1]], 0)
win32api.keybd_event(commands[sys.argv[1]], hwcode)
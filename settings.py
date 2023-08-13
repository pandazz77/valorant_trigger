from win32api import GetSystemMetrics

# DO NOT CHANGE

WIDTH = int(GetSystemMetrics(0))
HEIGHT = int(GetSystemMetrics(1))

# TO CHANGE

# https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
KEY_ACTIVATE = 0x48 # H 
KEY_EXIT = 0x4C # L
WAIT_KEY = 20
SCREEN_OFFSET = 5
ERR_OFFSET = 20
BBOX = tuple(int(x) for x in (WIDTH/2-SCREEN_OFFSET,HEIGHT/2-SCREEN_OFFSET,WIDTH/2+SCREEN_OFFSET,HEIGHT/2+SCREEN_OFFSET))
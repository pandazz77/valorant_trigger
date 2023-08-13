import cv2
import mss
import numpy as np
import sys
import settings as s
import ctypes

user32 = ctypes.WinDLL('user32', use_last_error = True)
MEM_ENTRY = np.random.randint(0,256,(s.SCREEN_OFFSET*2,s.SCREEN_OFFSET*2,4),dtype=np.uint8)
screen_mem = [MEM_ENTRY,MEM_ENTRY]
mse_mem = 0
switch = -1
activated = False

def key_pressed(key:int):
    if user32.GetKeyState(key)>1: return True
    return False

def lmb():
    user32.mouse_event(0x2)
    user32.mouse_event(0x4)

def mse(img1,img2): # mean squared error
    h,w = img1.shape[0:2]
    diff = cv2.subtract(img1,img2)
    err = np.sum(diff**2)
    mse = err/(float(h*w))
    return mse

while True:
    screen = mss.mss().grab(s.BBOX)
    #screen = ImageGrab.grab(bbox=s.BBOX)
    np_array = np.array(screen)
    switch*=-1
    screen_mem[switch] = np_array
    mse_value = mse(screen_mem[0],screen_mem[1])
    
    # activate by key
    if key_pressed(s.KEY_ACTIVATE):
        activated = True
    else:
        activated = False

    # exit by key
    if key_pressed(s.KEY_EXIT): sys.exit(1)

    # trigger event
    if (mse_value+s.ERR_OFFSET<mse_mem or mse_value-s.ERR_OFFSET>mse_mem) and activated:
        lmb()
        print(mse_value,mse_mem)
        print("TRIGGER")
    mse_mem = mse_value

    #cv2.imshow("Screen",np_array)
    key = cv2.waitKey(s.WAIT_KEY)
import numpy as np
from PIL import ImageGrab
import cv2
import time
import pygetwindow
import pyautogui

past_time = time.time()
while(True):
    titles = pygetwindow.getAllTitles()
    window = pygetwindow.getWindowsWithTitle('Plant VS Zombies Game')[0]
    left, top, right, bottom = window.left, window.top, window.right, window.bottom
    printscreen_pil = ImageGrab.grab(bbox=(left, top, right, bottom))
    print("Loop took {} seconds!".format(time.time()-past_time))
    past_time = time.time()
    cv2.imshow('window', cv2.cvtColor(np.array(printscreen_pil), cv2.COLOR_BGR2RGB))
    loc = pyautogui.locateCenterOnScreen('AI_pictures\sunshine.PNG')
    if loc != None:
        pyautogui.click(loc)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

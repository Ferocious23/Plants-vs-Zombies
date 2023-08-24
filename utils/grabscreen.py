import numpy as np
from PIL import ImageGrab
import cv2
import time
import pygetwindow
import pyautogui

# Load the template image
template = cv2.imread('AI_pictures\sunshine.PNG', cv2.IMREAD_GRAYSCALE)
template_height, template_width = template.shape

past_time = time.time()
while True:
    titles = pygetwindow.getAllTitles()
    window = pygetwindow.getWindowsWithTitle('Plant VS Zombies Game')[0]
    left, top, right, bottom = window.left, window.top, window.right, window.bottom
    printscreen_pil = ImageGrab.grab(bbox=(left, top, right, bottom))
    print("Loop took {} seconds!".format(time.time() - past_time))
    past_time = time.time()
    screenshot = cv2.cvtColor(np.array(printscreen_pil), cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.8
    if max_val >= threshold:
        top_left = max_loc
        bottom_right = (top_left[0] + template_width, top_left[1] + template_height)

        # Draw a rectangle around the match on the screenshot
        cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)

        # Click on the center of the match
        match_center_x = (top_left[0] + bottom_right[0]) // 2
        match_center_y = (top_left[1] + bottom_right[1]) // 2
        pyautogui.click(left + match_center_x, top + match_center_y)
        pyautogui.mouseDown()
        pyautogui.mouseUp()

    cv2.imshow('window', screenshot)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

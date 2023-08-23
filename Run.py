import sys
import pygame as pg
import os
import pyautogui
import subprocess
import time

num = 0
def wait_and_click(image_path):
    done = False
    while not done:
        loc = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
        if loc is not None:
            print(loc)
            pyautogui.moveTo(loc)
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
            done = True
        else:
            time.sleep(1)

image_paths = ['AI_pictures/grave.png', 'AI_pictures/sunflower_test.png', 'AI_pictures/Scary_Peashooter.PNG', 'AI_pictures/Sasquach.PNG', 'AI_pictures/Cold_peashooter.PNG', 'AI_pictures/trio.PNG', 'AI_pictures/blocker.PNG', 'AI_pictures/Chille.PNG', 'AI_pictures/Cherry.PNG', 'AI_pictures/Play.PNG']

for path in image_paths:
    print(path)
    wait_and_click(path)
    num += 1
    if num == 10:
        from utils import grabscreen

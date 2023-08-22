import pyautogui
import time

# Adjust these values based on your screen resolution and game window position
game_window_x = 0
game_window_y = 0

# Coordinates of the grid cells where plants can be placed
grid_cells = [(200, 300), (300, 300), (400, 300), (500, 300)]

def mouse_down(x, y):
    pyautogui.mouseDown(x=game_window_x + x, y=game_window_y + y)

def mouse_up(x, y):
    pyautogui.mouseUp(x=game_window_x + x, y=game_window_y + y)

def plant_sunflower():
    x, y = grid_cells[0]
    mouse_down(x, y)
    time.sleep(0.2)  # Adjust the delay as needed
    mouse_up(x, y)

def main():
    print("Starting Plants vs. Zombies AI")
    time.sleep(3)  # Give you time to focus on the game

    while True:
        # Plant a sunflower every 10 seconds
        plant_sunflower()
        time.sleep(10)

if __name__ == "__main__":
    main()

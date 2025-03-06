from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class DinoBot:
    def __init__(self, replaybtn, dino):
        self.replaybtn = replaybtn
        self.dino = dino

    def restartgame(self):
        pyautogui.click(self.replaybtn)

    def jump(self):
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')

    def grabimage(self):
        box = (self.dino[0] + 70, self.dino[1], self.dino[0] + 150, self.dino[1] + 60)
        image = ImageGrab.grab(box)       
        grayImage = ImageOps.grayscale(image)
        a = array(grayImage.getcolors())
        return a.sum()

    def start(self):
        self.restartgame()
        while True:
            if self.grabimage() != 1447:
                self.jump()
            time.sleep(0.1)

def main():
    replaybtn = (1280, 524)
    dino = (982, 532)
    time.sleep(3)
    print(pyautogui.position())  # Двигайте мышью и смотрите координаты
    bot = DinoBot(replaybtn, dino)
    bot.start()

if __name__ == "__main__":
    main()

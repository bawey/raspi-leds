import sys
import board
import neopixel
import time
import random

RED=(255,0,0)
BLUE=(0,255,0)
GREEN=(0,0,255)
LIME=(100, 155, 0)
YELLOW=(200,55,0)
ORANGE=(220,25,0)
VIOLET=(155, 0, 100)
WHITE=(85,85,85)

class LedStrip:
    def __init__(self, pixels_count: int):
        self.pixels_count = pixels_count
        self.pixels = neopixel.NeoPixel(board.D18, self.pixels_count, pixel_order=neopixel.RGB, auto_write=False)
        self.pixels.auto_write = False
        self.sleep_duration = 0.008

    def switch_off(self):
        for i in range(0, self.pixels_count):
            self.pixels[i] = (0, 0, 0)
        self.pixels.show()

    def embers(self):
        colors = [ORANGE, YELLOW]
        while True:
            try:
                idx = random.randrange(0, self.pixels_count)
                color_idx = random.randrange(0,len(colors))
                self.pixels[idx] = colors[color_idx]
                time.sleep(self.sleep_duration)
                self.pixels.show()
            except KeyboardInterrupt:
                print('Keyboard interrupt received, exiting soon...')
                break;

    def start(self):
        for i in range(0, self.pixels_count):
            self.pixels[i] = (155, 100, 0)
        self.pixels.show()


if __name__ == '__main__':
    leds = LedStrip(66)
    leds.embers()
    leds.switch_off()

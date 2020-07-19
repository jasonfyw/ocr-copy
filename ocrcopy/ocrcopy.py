from pynput import mouse
import pyscreenshot
import pytesseract
import pyperclip
import numpy as np
from PIL import ImageOps, ImageEnhance

"""
Handles the backend stuff
"""
class OCRCopy():
    def __init__(self, langs):
        self.langs = langs

        # start a mouse listener 
        self.x1, self.x2, self.y1, self.y2 = 0, 0, 0, 0
        with mouse.Listener(on_click = self.on_click) as listener:
            listener.join()

        # once the area has been selected, proceed with taking the screen shot and processing it
        if not (self.x1 == self.x2 and self.y1 == self.y2):
            img = self.get_screenshot(self.x1, self.y1, self.x2, self.y2)
            img = self.preprocess_image(img)
            text = self.recognise_text(img)

            pyperclip.copy(text)

            # debugging:
            # img.show()
        
    """
    Input monitoring function
    """
    def on_click(self, x, y, button, pressed):
        if pressed and str(button) == 'Button.left':
            self.x1, self.y1 = x, y
        elif str(button) == 'Button.left':
            self.x2, self.y2 = x, y
            return False

    """
    Getting image and processing it
    """
    def get_screenshot(self, x1, y1, x2, y2):
        # accounting for different directions to draw rectangle from
        if x2 >= x1 and y2 <= y1:
            bbox = (x1, y2, x2, y1)
        elif x2 <= x1 and y2 <= y1:
            bbox = (x2, y2, x1, y1)
        elif x2 <= x1 and y2 >= y1:
            bbox = (x2, y1, x1, y2)
        else: 
            bbox = (x1, y1, x2, y2)
        img = pyscreenshot.grab(bbox = bbox)
        return img

    def preprocess_image(self, img):
        # convert to greyscale
        img = img.convert('L') 

        # detect a dark background and invert image
        if np.mean(img) < 100:
            img = ImageOps.invert(img)

        # increase contrast
        img = ImageEnhance.Contrast(img).enhance(1.5)

        return img

    def recognise_text(self, img):
        # blanket detect a bunch of common languages/scripts (at the detriment of speed)
        config = '--oem 3 -l {}'.format(self.langs)
        text = pytesseract.image_to_string(img, config = config)

        return text

from pynput import mouse, keyboard
import pyscreenshot
import pytesseract
import pyperclip
import numpy as np
from PIL import ImageOps, ImageEnhance

class OCRCopy():
    def __init__(self):
        with keyboard.GlobalHotKeys({
            '<cmd>+<shift>+6': self.activate_shortcut
        }) as h:
            h.join()

    def on_click(self, x, y, button, pressed):
        if pressed and str(button) == 'Button.left':
            self.x1, self.y1 = x, y
        elif str(button) == 'Button.left':
            self.x2, self.y2 = x, y
            return False

    def get_screenshot(self, x1, y1, x2, y2):
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
        img = img.convert('L') 

        # print(np.mean(img))
        if np.mean(img) < 100:
            img = ImageOps.invert(img)

        img = ImageEnhance.Contrast(img).enhance(1.5)

        return img

    def recognise_text(self, img):
        config = r'--oem 3 -l eng'
        text = pytesseract.image_to_string(img, config = config)

        return text

    def activate_shortcut(self):
        self.x1, self.x2, self.y1, self.y2 = 0, 0, 0, 0
        with mouse.Listener(on_click = self.on_click) as listener:
            listener.join()

        img = self.get_screenshot(self.x1, self.y1, self.x2, self.y2)
        img = self.preprocess_image(img)
        text = self.recognise_text(img)

        pyperclip.copy(text)
        # img.show()
    

if __name__ == "__main__":
    ocrcopy = OCRCopy()
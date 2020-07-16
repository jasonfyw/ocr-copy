from pynput import mouse, keyboard
import pyscreenshot
import pytesseract
import pyperclip

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

    def get_screenshot(self, bbox):
        img = pyscreenshot.grab(bbox = bbox)
        return img

    def copy_to_clipboard(self, img):
        text = pytesseract.image_to_string(img)
        pyperclip.copy(text)

    def activate_shortcut(self):
        self.x1, self.x2, self.y1, self.y2 = 0, 0, 0, 0
        with mouse.Listener(on_click = self.on_click) as listener:
            listener.join()

        img = self.get_screenshot((self.x1, self.y1, self.x2, self.y2))
        self.copy_to_clipboard(img)
    

if __name__ == "__main__":
    ocrcopy = OCRCopy()
from pynput import mouse, keyboard
import pyscreenshot
import pytesseract
import pyperclip
import numpy as np
from PIL import ImageOps, ImageEnhance
import pyglet
import tkinter as tk


class Overlay():
    def __init__(self, root, width, height, x, y):
        self.width, self.height = width, height
        self.x, self.y = x, y

        self.overlay = tk.Toplevel(root)
        self.frame = tk.Frame(self.overlay)
        self.frame.pack(fill = tk.BOTH, expand = tk.YES)

        self.rect = None
        self.rect_startx = None
        self.rect_starty = None

        self.configure_canvas()
        self.configure_overlay()

    def configure_canvas(self):
        self.canvas = tk.Canvas(self.frame, cursor = 'cross', bg = '#ffffff')
        self.canvas.pack(fill = tk.BOTH, expand = tk.YES)

        self.canvas.bind('<ButtonPress-1>', self.handle_button_press)
        self.canvas.bind('<B1-Motion>', self.handle_move_press)
        self.canvas.bind('<ButtonRelease-1>', self.handle_button_release)

    def configure_overlay(self):
        geometry = '{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y)

        self.overlay.bind_all('<Configure', )
        self.overlay.geometry(geometry)
        self.overlay.attributes('-transparent', True)
        self.overlay.attributes('-alpha', 0.1)
        self.overlay.lift()
        self.overlay.attributes('-topmost', True)

        self.overlay.bind('<Configure>', lambda e: self.overlay.geometry(geometry)) 
        self.overlay.bind('<ButtonPress-1>', lambda e: print(e.x_root, e.y_root))   

    """
    Handle Canvas input events
    """
    def handle_button_press(self, event):
        self.rect_startx = self.canvas.canvasx(event.x)
        self.rect_starty = self.canvas.canvasy(event.y)

        self.rect = self.canvas.create_rectangle(
            self.rect_startx, 
            self.rect_starty, 
            self.rect_startx, 
            self.rect_starty, 
            outline = '#ff0000',
            width = 2,
            fill = '#bbbbbb'
        )

    def handle_move_press(self, event):
        self.canvas.coords(self.rect, self.rect_startx, self.rect_starty, event.x, event.y)

    def handle_button_release(self, event):
        self.canvas.delete(self.rect)

class OverlayController():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('0x0')
        self.root.withdraw()

        self.overlays = []
        self.create_overlays()

        self.root.mainloop()

    def create_overlays(self):
        for i, screen in enumerate(pyglet.window.get_platform().get_default_display().get_screens()):
            x, y, w, h = screen.x, screen.y, screen.width, screen.height
            self.overlays.append(Overlay(self.root, w, h, x, y))

    def destroy(self):
        for overlay in self.overlays:
            overlay.overlay.destroy()
            self.root.destroy()


class OCRCopy():

    """
    Input monitoring functions
    """
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

    """
    Getting image and processing it
    """
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

    """
    Main shortcut functionality
    """
    def activate_shortcut(self):
        self.x1, self.x2, self.y1, self.y2 = 0, 0, 0, 0
        with mouse.Listener(on_click = self.on_click) as listener:
            listener.join()

        if not (self.x1 == self.x2 and self.y1 == self.y2):
            img = self.get_screenshot(self.x1, self.y1, self.x2, self.y2)
            img = self.preprocess_image(img)
            text = self.recognise_text(img)

            pyperclip.copy(text)
            # img.show()


if __name__ == "__main__":
    # ocrcopy = OCRCopy()
    thing = OverlayController()
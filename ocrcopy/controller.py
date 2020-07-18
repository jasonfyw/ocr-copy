import tkinter as tk
from pynput import keyboard
import pyglet

from overlay import Overlay
from ocrcopy import OCRCopy

"""
Application controller
"""
class Controller():
    def __init__(self):
        # setup overlay root app
        self.root = tk.Tk()

        # hide root app
        self.root.geometry('0x0')
        self.root.withdraw()

        self.overlays = []

        # setup and initialised non-blocking hotkey listener
        self.hotkey = {keyboard.Key.cmd, keyboard.Key.shift, keyboard.KeyCode(char = '6')}
        self.activated_keys = set()

        listener = keyboard.Listener(on_press = self.handle_keypress, on_release = self.handle_keyrelease)
        listener.start()

        self.root.mainloop()

    """
    Event handlers
    """
    def handle_keypress(self, key):
        if any([key in self.hotkey]):
            self.activated_keys.add(key)
            if all(k in self.activated_keys for k in self.hotkey):
                self.activate_shortcut()

    def handle_keyrelease(self, key):
        if any([key in self.hotkey]):
            try:
                self.activated_keys.remove(key)
            except KeyError:
                self.activated_keys = self.activated_keys 

    """
    Destroy Toplevel overlays after shortcut finish
    """
    def destroy_overlays(self):
        for overlay in self.overlays:
            overlay.overlay.destroy()
            del overlay
        self.overlays = []

    """
    Upon shortcut activation
    """
    def activate_shortcut(self):
        self.create_overlays()
        ocrcopy = OCRCopy()
        del ocrcopy

        self.destroy_overlays()

    def create_overlays(self):
        # use pyglet to get information about screen dimensions and positioning
        # not very efficient but after first load it gets faster
        # for some reason it throws horribles errors if i try to do anything else with it
        for screen in pyglet.window.get_platform().get_default_display().get_screens():
            x, y, w, h = screen.x, screen.y, screen.width, screen.height
            self.overlays.append(Overlay(self.root, w, h, x, y, self.destroy_overlays))

if __name__ == "__main__":
    thing = Controller()
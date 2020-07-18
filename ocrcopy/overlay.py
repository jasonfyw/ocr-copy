import tkinter as tk

"""
Class for a single overlay
"""
class Overlay():
    def __init__(self, root, width, height, x, y, destroy_overlays):
        self.width, self.height = width, height
        self.x, self.y = x, y

        self.overlay = tk.Toplevel(root)
        self.frame = tk.Frame(self.overlay)
        self.frame.pack(fill = tk.BOTH, expand = tk.YES)

        # pass in function to destroy all overlays in Controller
        self.destroy_overlays = destroy_overlays

        self.rect = None
        self.rect_startx = None
        self.rect_starty = None

        self.configure_canvas()
        self.configure_overlay()

    """
    Initialise and setup translucent overlays
    """
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
        # reach up to Controller and destroy overlays
        self.destroy_overlays()

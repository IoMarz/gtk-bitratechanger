import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="FFMPEG Frontend for GTK3")

        # Status Boolean
        self.working = False

        # Grid
        self.grid = Gtk.Grid()
        self.add(self.grid)

        # Onscreen Objects
        # Text field
        self.path_to_file = Gtk.Entry()
        self.path_to_file.set_text("<enter full path>")

        # Bitrate (in kb/s)
        self.new_video_birate = Gtk.Entry()
        self.new_video_birate.set_text("<enter video bitrate>")

        # GO button
        self.go_button = Gtk.Button()
        self.go_button.set_label("GO!")
        self.go_button.connect("clicked", self.go_button_event)

        # Status
        self.status = Gtk.Label()
        self.status.set_label("Status: Ready")

        # Add objects to the grid
        self.grid.add(self.path_to_file)
        self.grid.attach(self.new_video_birate, 1, 0, 2, 1)
        self.grid.attach_next_to(self.go_button, self.path_to_file, Gtk.PositionType.BOTTOM, 1, 2)
        #self.grid.attach_next_to(self.status, self.go_button, Gtk.PositionType.BOTTOM, 1, 2)
    
    # GO button event
    def go_button_event(self, widget):
        if (self.working == True):
            print("Already on a job!")
        if (self.working == False):
            #self.status.set_label("Status: Working...")
            self.working = True
            print("going!")
            video_path = self.path_to_file.get_text()
            new_bitrate = self.new_video_birate.get_text() + "k"
            os.system("ffmpeg -i " + video_path + " -b " + new_bitrate + " output.mp4")
            self.working = False

window = MainWindow()
window.resize(300, 100)
window.connect("delete_event", Gtk.main_quit)
window.show_all()
Gtk.main()
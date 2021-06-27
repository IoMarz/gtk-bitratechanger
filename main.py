import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
from datetime import date, datetime

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

        # Video type field
        self.video_type = Gtk.Entry()
        self.video_type.set_text("<enter type (.mp4, etc)>")

        # GO button
        self.go_button = Gtk.Button()
        self.go_button.set_label("GO!")
        self.go_button.connect("clicked", self.go_button_event)

        # Watermark
        self.watermark = Gtk.Label()
        self.watermark.set_label("By IoMarz/Skyler")

        # Add objects to the grid
        self.grid.add(self.path_to_file)
        self.grid.attach(self.new_video_birate, 1, 0, 2, 1)
        self.grid.attach_next_to(self.video_type, self.path_to_file, Gtk.PositionType.BOTTOM, 1, 2)
        self.grid.attach_next_to(self.watermark, self.video_type, Gtk.PositionType.BOTTOM, 1, 2)
        self.grid.attach_next_to(self.go_button, self.new_video_birate, Gtk.PositionType.BOTTOM, 1, 2)
    
    # GO button event
    def go_button_event(self, widget):
        if (self.working == True):
            print("Already on a job!")
        if (self.working == False):
            self.working = True
            print("going!")
            # Set input values to a string
            video_path = self.path_to_file.get_text()
            new_bitrate = self.new_video_birate.get_text()
            video_type_str = self.video_type.get_text()
            # Get system time for the file to prevent file override
            now = datetime.now()
            systime = now.strftime("%H-%M-%S")
            print(systime)
            # Check if the bitrate is all numbers
            if (new_bitrate.isdigit()):
                print("bitrate check success!")
            else:
                print("bitrate is not a number! defaulting to 1000kbs")
                new_bitrate = "1000"
            # Set the out file to a string so i dont get confused lmao
            out_file = "Out-" + str(systime) + video_type_str
            # Execute the command
            os.system("ffmpeg -i " + video_path + " -b " + new_bitrate + "k " + out_file)
            self.working = False

window = MainWindow()
window.resize(300, 100)
window.connect("delete_event", Gtk.main_quit)
window.show_all()
Gtk.main()
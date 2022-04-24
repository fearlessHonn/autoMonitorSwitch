from os import system
import rotatescreen

system(r'cmd /c "C:\Users\henlu\PycharmProjects\autoMonitorSwitch\DPEdit.exe 1 0 0 2 0 -1080"')
system(r'cmd /c "C:\Users\henlu\PycharmProjects\autoMonitorSwitch\nircmd.exe setprimarydisplay 2"')
screen = rotatescreen.get_secondary_displays()[0]
screen.set_landscape_flipped()
from fileinput import filename
import time 
import random
import os
import sys
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


fromdir='C:/Users/HP/OneDrive/Desktop'
todir='C:/Users/HP/OneDrive/Desktop/python'

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt','.py'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class Filemovement(FileSystemEventHandler):
    def on_created(self,event):
        name,ext=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                filename=os.path.basename(event.src_path)

                path1 = fromdir + '/' + filename
                path2 = todir + '/' + key
                path3 = todir + '/' + key + '/' + filename

                if os.path.exists(path2):
                    print("folder exists....")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("making folder.....")
                    os.makedirs(path2)
                    shutil.move(path1,path3)
                    time.sleep(1)
                    



eventhandler=Filemovement()
observer=Observer()
observer.schedule(eventhandler,fromdir,recursive=True)

observer.start()

while True:
    try:
        time.sleep(2)
        print("running.....")

    except KeyboardInterrupt:
        print("stop")
        observer.stop()
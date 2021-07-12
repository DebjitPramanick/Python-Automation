from watchdog import observers
from watchdog.events import FileSystemEventHandler
import json
import time
import os

class FileHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(home):
            source = home+"/"+filename
            new_folder = destination+"/"+filename
            os.rename(source, new_folder)

home = "Web Automation/File Saving Automation/test1"
destination = "Web Automation/File Saving Automation/test2"

event_handler = FileHandler()
observer = observers.Observer()
observer.schedule(event_handler, home, recursive=True)
observer.start()


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
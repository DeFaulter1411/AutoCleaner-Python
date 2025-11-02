import sys
import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class OnlyWatch:
    def
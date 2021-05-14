from datetime import datetime
from time import sleep
import webbrowser
import os

def get_date():
     date = datetime.now().strftime("%-d %B %Y")
     return date

def get_time():
    time = datetime.now().time().strftime("%H %M")
    return time

def make_file(name):
    try:
        os.mknod(name)
    except Exception:
        print("try again")

def grep(recorded_audio):
    command = 'grep ' + recorded_audio.split(' ')[1]
    os.system('gnome-terminal -- bash -c "{}; bash "'.format(command))

def cat(recorded_audio):
    command = 'cat ' + recorded_audio.split(' ')[1]
    os.system('gnome-terminal -- bash -c "{}; bash "'.format(command))

def cd(recorded_audio):
    command  = 'cd ' + '/'+recorded_audio.split(' ')[2]
    os.system('gnome-terminal -- bash -c "{}; bash "'.format(command))


import os
import subprocess
from linux_utilities import *
from firewall import *

#subprocess.Popen('gedit')
s_log = 'gedit gedit'
os.system('gnome-terminal -- bash -c "{} "'.format(s_log))
#os.system('gedit gedit')
print("hello")
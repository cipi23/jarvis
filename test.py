import os
import subprocess
from linux_utilities import *
from firewall import *

audio = 'accept tcp 4521'
ipt_input(audio)
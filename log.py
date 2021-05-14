import os
import subprocess


def log_monitor():
    a_log = 'tail -f /var/log/auth.log' 
    s_log = 'tail -f /var/log/syslog'
    os.system('gnome-terminal -- bash -c "{}; bash "'.format(a_log))
    os.system('gnome-terminal -- bash -c "{}; bash "'.format(s_log))

def last_log():
    os.system('head -n 15 /var/log/auth.log > log')
    os.system('head -n 15 /var/log/syslog >> log')
    a = 'gedit log'
    os.system('gnome-terminal -- bash -c "{} "'.format(a))
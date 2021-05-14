import os


def ipt_input(recorded_audio):
    p = recorded_audio.split(' ')[1]
    dport = recorded_audio.split(' ')[2]
    os.system('iptables -A INPUT -p {} --dport {} -j ACCEPT'.format(p, dport))
    print('Command executed: iptables -A INPUT -p {} --dport {} -j ACCEPT'.format(p, dport))


def ipt_block(recorded_audio):
    p = recorded_audio.split(' ')[1]
    dport = recorded_audio.split(' ')[2]
    os.system('iptables -A INPUT -p {} --dport {} -j DROP'.format(p, dport))
    print('Command executed: iptables -A INPUT -p {} --dport {} -j ACCEPT'.format(p, dport))

def ipt_route(audio):
    pass


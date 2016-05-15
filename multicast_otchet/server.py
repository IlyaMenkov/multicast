import subprocess
import shlex

import subprocess
HOST = "localhost"
PORT = "4212"
password = "123"
PATH_TO_FILE = "/home/imenkov/test_vlc.mp4"

def start_server(password="123"):
    cmd = 'vlc --ttl 30 --color -I telnet --telnet-password %s' % password
    args = shlex.split(cmd)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.communicate()[0]
    print result





start_server(password=password)

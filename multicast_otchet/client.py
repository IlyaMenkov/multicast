__author__ = 'imenkov'
import subprocess
import shlex


def connect_to_vlc(url):
    cmd = 'vlc %s' % url
    args = shlex.split(cmd)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.communicate()[0]
    print result
connect_to_vlc('udp://@239.255.1.1')
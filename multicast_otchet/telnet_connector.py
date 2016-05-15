import subprocess
import shlex
import telnetlib

HOST = "localhost"
PORT = "4212"
password = "123"
PATH_TO_FILE = "/home/imenkov/test_vlc.mp4"

def connect_to_vlc(url):
    cmd = 'vlc %s' % url
    args = shlex.split(cmd)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.communicate()[0]
    print result

def settings_telnet(host="localhost", port='4212', path_to_file="/path/to/file.mv", password="123"):
    tn = telnetlib.Telnet(host=host, port=port)
    tn.read_until("Password: ")
    tn.write(password + "\n")
    tn.write("new channel1 broadcast enabled\n")
    tn.write("setup channel1 input %s\n" % path_to_file)
    tn.write("setup channel1 output #standard{access=udp{ttl=30},mux=ts{tsid=22,pid-video=23,pid-audio=24,pid-pmt=25,use-key-frames},dst=172.18.78.96,sap,name=\"Channel1\"}\n")
    tn.write("control channel1 play\n")
    tn.write("quit\n")
    print tn.read_all()
settings_telnet(host=HOST, port=PORT, path_to_file=PATH_TO_FILE, password=password)
connect_to_vlc('udp://@172.18.78.96')не е


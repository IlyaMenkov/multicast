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

def settings_telnet(host="localhost", port='4212',
                    path_to_file="/path/to/file.mv",
                    password="123",
                    count=1):
    tn = telnetlib.Telnet(host=host, port=port)
    tn.read_until("Password: ")
    tn.write(password + "\n")
    tn.write("new channel{0} broadcast enabled\n".format(str(count)))
    tn.write("setup channel{0} input {1}\n".format(str(count), path_to_file))
#    tn.write("setup channel1 output #standard{access=udp{ttl=30},mux=ts{tsid=22,pid-video=23,pid-audio=24,pid-pmt=25,use-key-frames},dst=172.18.78.117,sap,name=\"Channel1\"}\n")
    tn.write("setup channel{id} output #standard{{access=udp{{ttl=12}},mux=ts{{tsid=22,pid-video=23,pid-audio=24,pid-pmt=25,use-key-frames}},dst=239.255.1.{id},sap,name=\"Channel{id}\"}}\n".format(id=str(count)))
    tn.write("setup channel{0} loop\n".format(str(count)))
    tn.write("control channel{0} play\n".format(str(count)))
    tn.write("quit\n")
    print tn.read_all()
settings_telnet(host=HOST, port=PORT, path_to_file=PATH_TO_FILE, password=password)

def create_page(count=1):
    template = "embed type=\"application/x-vlc-plugin\" pluginspage=\"http://www.videolan.org\" version=\"VideoLAN.VLCPlugin.2\"  width=\"100%\"  height=\"100%\" id=\"vlc\" loop=\"yes\" autoplay=\"yes\" target=\"udp://@239.255.1.{0}\"></embed>".format(str(count))
    file = open("templates/newfile.html", "w")
    file.write(template)
    file.close()
create_page()

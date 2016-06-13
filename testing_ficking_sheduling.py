import subprocess
import shlex
import telnetlib
import time

def connect_to_vlc(url):
    cmd = 'vlc %s' % url
    args = shlex.split(cmd)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.communicate()[0]
    print result

class Settinger(object):
    def __init__(self, **kwargs):
    #    self.path_to_file = kwargs['path_to_file']
        self.pasword = kwargs['password']
        self.count = 1
   #     self.name = kwargs['name']
        self.host = kwargs['host']
        self.port = kwargs['port']


    def settings_telnet(self,
                        dt=None,
                        path_to_file="",
                        name="default"):

        ip_address = '239.255.1.6'.format(count=self.count)
        tn = telnetlib.Telnet(host=self.host, port=self.port)
        tn.read_until("Password: ")
        tn.write(password + "\n")
        tn.write("new channel1 broadcast enabled\n")
        tn.write("setup channel1 input {}\n".format(path_to_file))
        tn.write("setup channel1 output #standard{{access=udp{{ttl=12}},mux=ts{{tsid=22,pid-video=23,pid-audio=24,pid-pmt=25,use-key-frames}},dst=239.255.1.6,sap,name=\"Channel1\"}}\n".format(id=self.count))
    #    tn.write("setup channel{0} loop\n".format(str(count)))
        tn.write("new my_sched schedule enabled\n")
        tn.write("setup my_sched date {}\n".format(dt))
        tn.write("setup my_sched append control channel1 play\n")
        tn.write("quit\n")
        self.count += 1
        print tn.read_very_eager()
        print tn.read_very_eager()

# uncomment this string if u needs some debug
        create_page(count=self.count, name=name.format(self.count))
        return ip_address, self.count
# setup channel1 output #standard{access=udp{ttl=12},mux=ts{tsid=22,pid-video=23,pid-audio=24,pid-pmt=25,use-key-frames},dst=239.255.1.1,sap,name="Channel1"}
# setup channel1 output #standard{access=udp{ttl=12},mux=ts{tsid=22,pid-video=23,pid-audio=24,pid-pmt=25,use-key-frames},dst=239.255.1.1,sap,name="Channel1"}
def create_page(count=1, name="Name Of Translation is undefine", line_number=11):
    filename = "newfile{0}".format(count)
    # create new page and adding it to templates dirrectiry
    template = "<embed type=\"application/x-vlc-plugin\" " \
               "pluginspage=\"http://www.videolan.org\" " \
               "version=\"VideoLAN.VLCPlugin.2\"  " \
               "width=\"100%\"  " \
               "height=\"100%\" " \
               "id=\"vlc\" loop=\"yes\"" \
               " autoplay=\"yes\"" \
               " target=\"udp://@239.255.1.6\">" \
               "</embed>".format(str(count))

    file = open("templates/{0}.html".format(filename), "w")
    file.write(template)
    file.close()
"""
    # adding new page to web_server
    link = "\n@app.route(\'/{filename}\')\n" \
           "def {filename}():\n" \
           "\treturn render_template(\'{filename}.html\')\n".format(filename=filename)
    file = "serv.py"
    with open(file) as f:
        lines = f.readlines()
    lines.insert(9, link)
    with open(file, 'w') as f:
        f.writelines(lines)

    #adding new page to index
    link = "\t<p><a href=\"{name}\">{tn}</a></p>\n".format(
                                                tn=name,
                                                name=filename)
    file = "templates/index.html"
    with open(file) as f:
        lines = f.readlines()
    lines.insert(line_number, link)
    with open(file, 'w') as f:
        f.writelines(lines)


"""
import datetime
#
##dt = now.strftime('%Y/ %M')
#tm = now.strftime('%H:%M:%S')
#print now.date().strftime('%D')
##print dt
#print tm

dt = now.strftime('%Y/%m/%d-%H:%M:%S')
print dt

print dt
HOST = "localhost"
PORT = "4212"
password = "123"
PATH_TO_FILE = "/home/imenkov/PycharmProjects/multicast/content/test_vlc.mp4"
new=Settinger(password='123', host='localhost', port='4212')
print new.settings_telnet(path_to_file='/test_vlc.mp4', dt=dt)
# #
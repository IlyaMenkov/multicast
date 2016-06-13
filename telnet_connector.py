import subprocess
import shlex
import telnetlib


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
        self.count += 1

        if dt:
            ip_address = '239.255.1.{}'.format(self.count)
            tn = telnetlib.Telnet(host=self.host, port=self.port)
            tn.read_until("Password: ")
            tn.write(password + "\n")
            tn.write("new channel{id} broadcast enabled\n".format(id=str(self.count)))
            tn.write("setup channel{id} input {path}\n".format(id=str(self.count),
                                                               path=path_to_file))
            tn.write("setup channel{id} output #standard{{access=udp{{ttl=12}},mux=ts{{tsid=22,pid-video=23,pid-audio=24,pid-pmt=25,use-key-frames}},dst=239.255.1.{id},sap,name=\"Channel{id}\"}}\n".format(id=str(self.count)))
    #        tn.write("setup channel{0} loop\n".format(str(count)))
            tn.write("new my_sched{id} schedule enabled\n".format(id=str(self.count)))
            tn.write("setup my_sched{id} date {dt}\n".format(id=str(self.count),
                                                             dt=dt))
            tn.write("setup my_sched{id} append control channel{id} play\n".format(id=str(self.count)))
            tn.write("quit\n")
            #print tn.read_very_eager()
            print tn.read_very_lazy()
        else:
            ip_address = '239.255.1.{count}'.format(count=self.count)
            tn = telnetlib.Telnet(host=self.host, port=self.port)
            tn.read_until("Password: ")
            tn.write(password + "\n")
            tn.write("new channel{0} broadcast enabled\n".format(str(self.count)))
            tn.write("setup channel{0} input {1}\n".format(str(self.count), path_to_file))
            tn.write("setup channel{id} output #standard{{access=udp{{ttl=12}},mux=ts{{tsid=22,pid-video=23,pid-audio=24,pid-pmt=25,use-key-frames}},dst=239.255.1.{id},sap,name=\"Channel{id}\"}}\n".format(id=self.count))
    #        tn.write("setup channel{0} loop\n".format(str(count)))
            tn.write("control channel{0} play\n".format(str(self.count)))
            tn.write("quit\n")
            print tn.read_all()

# uncomment this string if u needs some debug
        create_page(count=self.count, name=name.format(self.count))
        return ip_address, self.count
# setup channel1 output #standard{access=udp{ttl=12},mux=ts{tsid=22,pid-video=23,pid-audio=24,pid-pmt=25,use-key-frames},dst=239.255.1.1,sap,name="Channel1"}
#
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
               " target=\"udp://@239.255.1.{0}\">" \
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


HOST = "localhost"
PORT = "4212"
password = "123"
#PATH_TO_FILE = "/home/imenkov/PycharmProjects/multicast/content/test_vlc.mp4"
#new=Settinger(password='123', host='localhost', port='4212')
#print new.settings_telnet(path_to_file='/test_vlc.mp4')
#
#
#import datetime
#now = datetime.datetime.now()
#dt = now.strftime('%Y/%m/%d-%H:{}:%S').format(str(int(now.strftime('%M'))+1))
#print new.settings_telnet(path_to_file='/test_vlc.mp4', dt=dt)
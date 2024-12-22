import command as cmd
import socket

class IPV4(cmd.Command):
    def __init__(self):
        super().__init__(name="ipv4", description="tells the ipv4 adress", capitalName="I P V 4", version=0.4)



    def run(self, argv):
        ip = self.get_ip_address()
        print(ip)


    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
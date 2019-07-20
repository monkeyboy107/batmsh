import subprocess
from time import sleep

class procs:
    def __init__(self, jar_name):
        self.jar_name = jar_name
        McServer = 'java -jar -Xms1G' \
                   ' -Xmx4G ' + jar_name,
        self.minecraft = subprocess.Popen(McServer,
                                     stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     shell=True)
        sleep(60)
        self.server_started = False
        self.mc_runner()

    def talk_mc(self, command):
        command = self.byteconvert(command)
        sleep(1)
        self.minecraft.stdin.write(command)

    def byteconvert(self, string):
        return string.encode('utf-8')

    def byteUNconverter(self, byte):
        return str(byte, 'utf-8')

    def mc_runner(self):
        self.talk_mc('op monkeybpy107')
        while True:
            self.talk_mc('say Server start')
            if self.minecraft.stdout.readline() != b'':
                try:
                    #if self.server_started == False:
                    print(self.byteUNconverter(self.minecraft.stdout.readline()).split(" ")[1:-1])
                    #self.server_started = True
                except IndexError:
                    None
                print(self.byteUNconverter(self.minecraft.stdout.readline()), end='')


p = procs('server.jar')

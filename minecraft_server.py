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
        self.server_started = False
        self.mc_runner()

    def talk_mc(self, command):
        command = self.byteconvert(command)
        print(command)
        sleep(1)
        self.minecraft.communicate(command)

    def byteconvert(self, string):
        return string.encode('utf-8')

    def byteUNconverter(self, byte):
        return str(byte, 'utf-8')

    def mc_runner(self):
        while True:
            output = self.minecraft.stdout.readline()
            if output == []:
                break
            if output:
                print(output.strip())
            try:
                if output.split()[3] == b'Done':
                    self.server_started = True
            except IndexError:
                None
            if self.server_started:
                self.talk_mc('op monkeyboy107')

if __name__ == '__main__':
    p = procs('server.jar')

import subprocess
from time import sleep
import py_compile
import os.path

py_compile.compile(os.path.basename(__file__))


class procs:
    def __init__(self, jar_name):
        print('Instantiating procs in', __name__)
        self.jar_name = jar_name
        McServer = 'java -jar -Xms1G' \
                   ' -Xmx4G ' + jar_name,
        self.minecraft = subprocess.Popen(McServer,
                                     stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     shell=True)
        self.server_started = False
        #self.mc_runner()

    def talk_mc(self, command):
        print('Talking to minecraft server')
        command = self.byteconvert(command)
        print(command)
        sleep(1)
        self.minecraft.communicate(command)

    def byteconvert(self, string):
        print('Converting to bytes')
        return string.encode('utf-8')

    def byteUNconverter(self, byte):
        print('Converting back to utf-8')
        return str(byte, 'utf-8')

    def mc_runner(self):
        print('Running minecraft')
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

    def accept_eula(self, accept='false', eula_file='eula.txt'):
        if type(accept) == bool:
            accept = str(accept)
        accept = 'eula=' + accept
        with open(eula_file, 'w') as eula:
            eula.write(accept)

if __name__ == '__main__':
    p = procs('server.jar')
    #p.mc_runner()

import subprocess
from time import sleep
import multiprocessing
import py_compile
import os.path
from os import remove

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
        self.commands_to_be_run = []
        self.command_file = '.command'

    def start_server(self):
        talker_thread = self
        runner_thread = self
        runner = multiprocessing.Process(target=runner_thread.mc_runner(), args=runner_thread)
        talker = multiprocessing.Process(target=talker_thread.talk_mc_runner(), args=talker_thread)
        talker.start()
        runner.start()
        talker.join()
        runner.join()

    def append_commands(self, commands):
        print('appending_commands is started with: ' + commands)
        self.commands_to_be_run.append(commands)
        try:
            with open(self.command_file, 'r') as command:
                for line in command.read().split('\n'):
                    command.append(line)
        except FileNotFoundError:
            None
        with open(self.command_file, 'w+') as command:
            for line in command:
                command.write(line)

    def talk_mc_runner(self):
        print('Starting talk_mc_runner')
        while True:
            try:
                with open(self.command_file, 'r') as commands:
                    for line in commands.read().split('\n'):
                        self.commands_to_be_run.append(line)
                    remove(self.command_file)
            except FileNotFoundError:
                None
            if self.server_started:
                try:
                    self.talk_mc(self.commands_to_be_run.pop())
                    sleep(30)
                except IndexError:
                    None
            if not self.commands_to_be_run == []:
                print(self.commands_to_be_run)

    def talk_mc(self, command):
        print('Talking to minecraft server')
        command = self.byteconvert(command)
        print(command)
        sleep(20)
        try:
            self.minecraft.communicate(command, timeout=1)
        except subprocess.TimeoutExpired:
            None
        print('Done with talk_mc')

    def byteconvert(self, string):
        print('Converting to bytes')
        return string.encode('utf-8')

    def byteUNconverter(self, byte):
        print('Converting back to utf-8')
        return str(byte, 'utf-8')

    def mc_runner(self):
        print('Running minecraft')
        while True:
            #print('Back in the loop for the mc_runner')
            output = self.minecraft.stdout.readline()
            if output == []:
                print('Breaking the mc_runner loop')
                break
            if output:
                print(output.strip())
            try:
                if output.split()[3] == b'Done':
                    self.server_started = True
            except IndexError:
                None
            if self.server_started:
                self.append_commands('op monkeyboy107')

    def accept_eula(self, accept=False, eula_file='eula.txt'):
        if type(accept) == bool:
            accept = str(accept)
        accept = 'eula=' + accept
        with open(eula_file, 'w') as eula:
            eula.write(accept)

if __name__ == '__main__':
    p = procs('server.jar')
    p.accept_eula(accept=True)
    p.start_server()

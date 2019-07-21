import minecraft_dowloader
import minecraft_server
import jar_finder
import py_compile
import os.path

py_compile.compile(os.path.basename(__file__))


class Download:
    def __init__(self, url, version):
        self.url = url
        self.version = version
        self.jar = jar_finder.jar_finder(url)
        self.jar_version = self.jar.name_finder(self.jar.jar_finder(version))
        self.download_link = self.jar.jar_finder(version)

    def download_jar(self, server='server.jar', force_download=False):
        downloader = minecraft_dowloader.downloader(self.download_link, server)
        downloader.download()

class run_minecraft:
    def __init__(self, jar_name):
        self.mc_server = minecraft_server.procs(jar_name)

    def accept_eula(self, accept=False, eula_file='eula.txt'):
        self.mc_server.accept_eula(accept=accept, eula_file=eula_file)

if __name__ == '__main__':
    d = Download('https://getbukkit.org/download/craftbukkit', 0)
    d.download_jar()
    run = run_minecraft('server.jar')
    run.accept_eula(accept=True)
    run.mc_server.mc_runner()

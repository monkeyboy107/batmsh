import minecraft_dowloader
import jar_finder


class download:
    def __init__(self, url, version):
        self.url = url
        self.version = version
        self.jar = jar_finder.jar_finder(url)
        self.jar_version = self.jar.name_finder(self.jar.jar_finder(version))
        self.download_link = self.jar.jar_finder(version)

    def download_jar(self, server='server.jar'):
        downloader = minecraft_dowloader.downloader(self.download_link, server)
        downloader.download()


if __name__ == '__main__':
    d = download('https://getbukkit.org/download/craftbukkit', 1)
    d.download_jar()

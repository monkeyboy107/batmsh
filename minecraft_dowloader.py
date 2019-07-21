import requests
import os.path
import py_compile
import os.path

py_compile.compile(os.path.basename(__file__))


class downloader:
    def __init__(self, url, name):
        print('Instantiating downloader in', __name__)
        self.url = url
        self.name = name

    def download(self, force_download=False):
        print('Downloading the jar')
        if not os.path.exists(self.name) or force_download:
            print('Right before downloading, this sometimes takes a minute')
            request = requests.get(self.url)
            with open(self.name, 'wb') as jar:
                print('Done downloading')
                jar.write(request.content)
        else:
            print('File exists skipping')

if __name__ == '__main__':
    bukkit = downloader('https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14.3-R0.1-SNAPSHOT.jar', 'server.jar')
    bukkit.download()

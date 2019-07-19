import requests

class downloader:
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def download(self):
        request = requests.get(self.url)
        with open(self.name, 'wb') as jar:
            jar.write(request.content)

if __name__ == '__main__':
    bukkit = downloader('https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14.3-R0.1-SNAPSHOT.jar', 'server.jar')
    bukkit.download()
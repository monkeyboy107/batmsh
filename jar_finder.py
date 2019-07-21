import requests
from lxml import html
import py_compile
import os.path

py_compile.compile(os.path.basename(__file__))


class jar_finder:
    def __init__(self, url):
        print('Instantiating jar_finder in', __name__)
        self.url = url
        self.hrefs = ''
        self.site = self.find_site(self.url)
        self.scrapper()
        self.parser()

    def name_finder(self, jar_name):
        print("Finding the jar's name in name_finder")
        jar_name = jar_name.split('/')
        jar_name = jar_name[-1]
        jar_name = jar_name.replace('-', ' ')
        return jar_name[0:-4]

    def scrapper(self):
        print('Scrapping for hrefs')
        page = requests.get(self.url)
        root = html.fromstring(page.content)
        self.hrefs = root.xpath('//@href')

    def parser(self):
        print('Parsing')
        self.hrefs = self.find_url(self.hrefs, self.site)
        self.hrefs = self.find_download(self.hrefs)
        return self.hrefs

    def find_url(self, hrefs, site):
        print('Finding URL')
        sites = []
        for i in hrefs:
            if i[0:len(site)] == site:
                sites.append(i)
        return sites

    def find_site(self, url, ford_slash='/'):
        print('Finding the site')
        site = url.split(ford_slash)
        site = site[0:3]
        site = ford_slash.join(site)
        return site

    def find_download(self, sites, download='get', ford_slash ='/'):
        print('Finding the download links')
        getable = []
        url = self.site + ford_slash + download
        for site in sites:
            if site[0:len(url)] == url:
                getable.append(site)
        return getable

    def jar_finder(self, version):
        print('Finding the jar download link')
        page = requests.get(self.hrefs[version])
        root = html.fromstring(page.content)
        hrefs = root.xpath('//@href')
        return hrefs[33]


if __name__ == '__main__':
    jar = jar_finder('https://getbukkit.org/download/craftbukkit')
    for jar_files in range(len(jar.hrefs)):
        print(jar.jar_finder(jar_files), jar.name_finder(jar.jar_finder(jar_files)))

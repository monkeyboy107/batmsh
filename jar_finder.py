import requests
from lxml import html


class jar_finder:
    def __init__(self, url):
        self.url = url
        self.hrefs = ''
        self.site = self.find_site(self.url)

    def scrapper(self):
        page = requests.get(self.url)
        root = html.fromstring(page.content)
        self.hrefs = root.xpath('//@href')

    def parser(self):
        #for i in self.hrefs:
            #print(i)
        #print(len(self.site))
        self.hrefs = self.find_url(self.hrefs, self.site)
        self.hrefs = self.find_download(self.hrefs)
        #print(self.hrefs)
        return self.hrefs

    def find_url(self, hrefs, site):
        sites = []
        for i in hrefs:
            if i[0:len(site)] == site:
                sites.append(i)
        return sites

    def find_last_inter(self, iterable, value):
        index = ''.join(iterable).rindex(value)
        return index

    def find_site(self, url, fordslash='/'):
        site = url.split(fordslash)
        site = site[0:3]
        site = fordslash.join(site)
        return site

    def find_download(self, sites, download='get', fordslash = '/'):
        getable = []
        url = self.site + fordslash + download
        for site in sites:
            if site[0:len(url)] == url:
                getable.append(site)
        return getable

    def jar_finder(self, version):
        page = requests.get(self.hrefs[version])
        root = html.fromstring(page.content)
        hrefs = root.xpath('//@href')
        return hrefs[33]


if __name__ == '__main__':
    jar = jar_finder('https://getbukkit.org/download/craftbukkit')
    jar.scrapper()
    jar.parser()
    jar.jar_finder(0)
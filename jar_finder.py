import requests
from lxml import html


class jar_finder:
    def __init__(self, url):
        self.url = url
        self.hrefs = ''
        self.site = self.find_site(self.url)
        self.scrapper()
        self.parser()

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

    def find_download(self, sites, download='get', ford_slash ='/'):
        getable = []
        url = self.site + ford_slash + download
        for site in sites:
            if site[0:len(url)] == url:
                getable.append(site)
        return getable

    def jar_finder(self, version):
        page = requests.get(self.hrefs[version])
        root = html.fromstring(page.content)
        hrefs = root.xpath('//@href')
        return hrefs[33]

    def name_finder(self, jar_name):
        jar_name = jar_name.split('/')
        jar_name = jar_name[-1]
        jar_name = jar_name.replace('-', ' ')
        return jar_name[0:-4]


if __name__ == '__main__':
    jar = jar_finder('https://getbukkit.org/download/craftbukkit')
    for jar_files in range(len(jar.hrefs)):
        print(jar.jar_finder(jar_files), jar.name_finder(jar.jar_finder(jar_files)))
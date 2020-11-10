import re
import urllib.request

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html


def get_img(html):
    p = r'<img class = "BDE_Image" src = "([^"]+\.jpg)"'
    imglists = re.findall(p, html)
    for each in imglists:
        print(each)


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/5065009189'
    get_img(url_open(url))

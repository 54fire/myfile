import requests
from lxml import etree

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
'''
url = "http://aqd520.com"
response = requests.get(url)
#print(response.content.decode("utf-8"))
html = etree.HTML(response.content.decode())
elements_url  = html.xpath('//div[@class="caption"]//a/@href')
elements_title = html.xpath('//div[@class="caption"]//a/@title')
urls = []
for element_url in elements_url:
    element_url = url + element_url
    urls.append(element_url)
#print(elements_title)
'''

def download_vedio(url,name):
    r = requests.get(url)
    with open(name+".mp4","wb") as f:
        f.write(r.content)
        f.close()

sources = []
for n in range(47,208):
    url = "http://aqd520.com/videos/play/" + str(n)
    res = requests.get(url)
    html_er = etree.HTML(res.content.decode())
    sources.append(html_er.xpath("//video/source/@src")[0])

    for source in sources:
        m3u8 = requests.get(source)
        with open(source[-13:],"wb") as f:
            f.write(m3u8.content)
        movies_url = []
        file = open(source[-13:], 'rb')
        for line in file.readlines():
            line = str(line)[2:-3]
            if '.ts' in line:
                url_temp = source[:-13]
                movies_url.append(url_temp + line)
            else:
                continue
        for url in movies_url:
            movie = requests.get(url)
            with open(str(n) + ".ts","ab") as f:
                f.write(movie.content)
                f.close()
    sources = []
    print("next")

    #download_vedio(url,str(n))
    #print("next")
#print(urls)


'''
with open("a.mp4","wb") as f:
    f.write(response.content)
'''
import requests
from lxml import etree
url = "http://www.39gmgm.com"       #程序入口
response = requests.get(url)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
#print(response.content.decode("gbk"))
print(response.content.decode("gbk"))

'''
# 下载首页的视频
htmls = etree.HTML(response.content.decode("gbk"))
elements = htmls.xpath('//div[@class="videos"]/div')
webs = []
for element in elements:
    web = element.xpath('.//p/a/@href')
    webs.append(web[0] if len(web) > 0 else None)
urls = []
for web in webs:
    if web != None:
        url_t = url + web
    urls.append(url_t)

vedios = []
for url in urls:
    r = requests.get(url)
    r_html = etree.HTML(r.content.decode("gbk"))
    vedio = r_html.xpath('//source/@src')
    vedios.append(vedio[0])

# 下载视频，输入参数为url地址和保存名称。
def download_vedio(url,name):
    r = requests.get(url)
    with open(name+".mp4","wb") as f:
        f.write(r.content)
        f.close()

for vedio in vedios:
    download_vedio(vedio,vedio[-8:-5])
    print("next")
'''

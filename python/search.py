import requests
from lxml import etree

url = "http://www.36yeye.com/search.asp"
datas = {"type":"vedio","searchword":"教师".encode("gbk")}
responses = requests.post(url,data=datas)
responses_html = etree.HTML(responses.content.decode("gbk"))
page_elements = responses_html.xpath('//div[@class="pagination"]/ul/li')
page_url = page_elements[-2].xpath('./a/@href')[0]      #page_url 搜索的url
page_max = page_elements[-2].xpath('./a/text()')[0]     #page_max 页码的最大数

'''
@funcName: dowload_vedios
@function: 输入url以返回视频的url与title,并存入列表vedios_tmp
@Time : 2018-08-21
'''
def dowload_vedios(url):
    vedios_tmp = []
    responses = requests.get(url)
    responses_html = etree.HTML(responses.content.decode("gbk"))
    vedio_tmps = responses_html.xpath('//div[@class="video_box"]')
    # print(responses.content.decode("gbk"))
    for vedio_tmp in vedio_tmps:
        vedios = {}
        vedios["url"]   = vedio_tmp.xpath('./a/@href')[0]
        vedios["title"] = vedio_tmp.xpath('./a/img/@title')[0]
        vedios_tmp.append(vedios)
    return vedios_tmp
    # print(vedios_tmp)

'''
@funcName: get_vedios
@function: 输入视频的url与title，以下载视频并保存
@Time: 2018-08-21
'''
def get_vedios(url,title):
    r = requests.get(url)
    # print(r.content.decode("gbk"))
    r_element = etree.HTML(r.content.decode("gbk"))
    vedio_url = r_element.xpath('//script[@type="text/javascript"]/text()')[0].split(";")[-3].strip()[8:-2]
    print(title)
    r_vedio = requests.get(vedio_url)
    with open(title + ".mp4","wb") as f:
        f.write(r_vedio.content)
        f.close()


for i in range(2,int(page_max) + 1):
    url_tmp = url + page_url[:6] + str(i) + page_url[7:].strip("0")
    vedio_boxs = dowload_vedios(url_tmp)
    for vedio_box in vedio_boxs:
        get_vedios(vedio_box['url'],vedio_box['title'])
        print("next")

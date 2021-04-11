import requests
from bs4 import BeautifulSoup
import ffmpy3

search_keyword='司藤'
search_url='https://www.filmparadise.cn/vodsearch/-------------.html'
search_headers={
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
'origin': 'https://www.filmparadise.cn',
'referer': 'https://www.filmparadise.cn/vodtype/3.html'

}
search_datas={
    'wd':search_keyword
}
r=requests.post(url=search_url,headers=search_headers,data=search_datas)
r.encoding='utf-8'
server='https://www.filmparadise.cn'
search_html=BeautifulSoup(r.text,'lxml')
search_divs=search_html.find_all('div',class_='head')
url=server+search_divs[0].a.get('href')
name=search_divs[0].a.string
bs=BeautifulSoup(requests.get(url=url).text,'lxml')
lis=bs.find('div',id='playlist3').find_all('li')
urls=[]
for li in lis:
    urls.append(server+li.a.get('href'))
for i,url in enumerate(urls):
    print("第{0}集正在下载".format(i))
    print(url)
    bs=BeautifulSoup(requests.get(url=url).text, 'lxml')
#ffmpy3.FFmpeg(executable='/usr/local/ffmpeg/bin/ffmpeg',inputs={'https://www.kkarm.com:65/20191126/eKeoBOS7/index.m3u8': None}, outputs={'第003集.mp4':None}).run()

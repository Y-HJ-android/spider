import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
from contextlib import closing
from tqdm import tqdm
import os
if __name__=='__main__':
    save_dir="妖神记"
    if save_dir not in os.listdir('.'):
        os.mkdir(save_dir)
    #章节名称和地址
    name=[]
    uu=[]
    url='https://www.dmzj.com/info/yaoshenji.html'
    parse=BeautifulSoup(requests.get(url=url).text,'lxml')
    sum=parse.find('ul',class_='list_con_li').find_all('a')
    for i in sum:
        name.insert(0,i.text)
        uu.insert(0,i.get('href'))
    for id,chapter_url in enumerate(tqdm(uu)):
        chapter_name=name[id]
        while '.' in chapter_name:
            chapter_name=chapter_name.replace('.','')
        chapter_dir=os.path.join(save_dir,chapter_name)
        if chapter_name not in os.listdir(save_dir):
            os.mkdir(chapter_dir)
        parse = BeautifulSoup(requests.get(url=chapter_url).text, 'lxml')
        script_info=parse.script
        pics=re.findall('\d{13,14}',str(script_info))
        for idx,pic in enumerate(pics):
            if len(pic)==13:
                pics[idx]=pic+'0'
        pics=sorted(pics,key=lambda x:int(x))
        try:
            hou=re.findall('\|(\d{5})\|',str(script_info))[0]
            qian=re.findall('\|(\d{4})\|', str(script_info))[0]
        except IndexError as e:
            print(chapter_name+"访问不到")
            continue
        for i,pic in enumerate(pics):
            if pic[-1]=='0':
                url = 'https://images.dmzj1.com/img/chapterpic/' + qian + '/' + hou + '/' + pic[:-1] + '.jpg'
            else:
                url='https://images.dmzj1.com/img/chapterpic/'+qian+'/'+hou+'/'+pic+'.jpg'
            #没有反扒手段可以用
            #urlretrieve(url,'1.jpg')
            #针对反扒手段
            download_header={
                'Referer':chapter_url
            }
            with closing(requests.get(url=url,headers=download_header,stream=True)) as response:
                chunk_size=1024
                content_size=int(response.headers['content-length'])
                if response.status_code==200:
                    #print('文件大小:%.2f KB'%(content_size/chunk_size))
                    with open(chapter_dir+'/'+"%03d"%(i+1)+'.jpg','wb')as file:
                        for data in response.iter_content(chunk_size=chunk_size):
                            file.write(data)
                else:
                    print('连接异常')
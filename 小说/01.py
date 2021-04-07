import requests
from bs4 import BeautifulSoup
def get_content(url):
    req=requests.get(url=url)
    req.encoding="utf-8"
    html=req.text
    bs=BeautifulSoup(html,'lxml')
    texts=bs.find('div',id='content')
    return texts.text.strip().split('\xa0'*4)
if __name__=='__main__':
    book_name="诡秘之王.txt"
    server='https://www.vbiquge.com'
    target='https://www.vbiquge.com/98_98265/'
    req=requests.get(url=target)
    req.encoding='utf-8'
    html=req.text
    bs=BeautifulSoup(html,'lxml')
    texts = bs.find('div', id='list')
    chapters=texts.findAll('a')
    for chapter in chapters:
        chapter_name=chapter.string
        chapter_content=get_content(server+chapter.get('href'))
        with open(book_name,'a',encoding='utf-8') as file:
            file.write('                     '+chapter_name)
            file.write('\n')
            file.write("\n    ".join(chapter_content))
            file.write('\n')
        print(chapter_name+"下载完成")

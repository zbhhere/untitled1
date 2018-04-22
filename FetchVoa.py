import json

import requests
import os
from multiprocessing.pool import Pool
from pyquery import PyQuery as py
import EncrypFile

from bs4 import BeautifulSoup
import re

base_url='http://www.51voa.com/VOA_Standard_'
behalf_url='_archiver.html'

base_actical_url='http://www.51voa.com'


headers={
    'Host':'www.51voa.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

def write_to_file(actical):
    filename=str(actical['title'])+'.txt'
    with open('VOA2/'+filename,'a',encoding='utf-8') as f:
        f.write(json.dumps(actical['content'],ensure_ascii=False))
    print('写入成功')
    f.close()

def get_acticals(actical_url):
    url=base_actical_url+actical_url
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    if response.status_code==200:
         html=response.text
         # actical_urls = BeautifulSoup(html, 'lxml')
         pattern1 = re.compile(r'[|"\/\\:<>?*]+', re.S)  #不能使用的只有/ \ : * ?" < > | 这几个符号.
         doc=py(html)

         pattern2=re.compile(r'[\u4e00-\u9fa5]+', re.S)
         title=doc('div').filter('#title').text()
         title=re.sub(pattern1,'',title)
         content=doc('p').text()

         #有些网友是br内装内容
         pattern3=re.compile(r'[\s]*',re.S)

         if re.match(pattern3,content):
            content=doc('div').filter('#content').text()
         content=re.sub(pattern2,'',content)


         # title=actical_url.div.title.string
         # print(actical_urls)
         yield {
             'title':title,
             'content':content
         }

    return None

def get_page(page):
    url = base_url + str(page) + behalf_url
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    if response.status_code==200:
        return response.text
    return None


def get_page_url(html):
    patern=re.compile(r'class="adsbygoogle".*?</script>',re.S)
    html=re.sub(patern,'',html)

    patern=re.compile(r'<head>.*id="list"',re.S)
    html=re.sub(patern,'',html)
    # print(html)
    patern=re.compile(r"(/VOA_Standard_English/.*?\d{4,5}.html)",re.S)
    items=re.findall(patern,html)
    for item in items:
        for actical in get_acticals(item):
          write_to_file(actical)



def main(page):
    html = get_page(page)
    get_page_url(html)


if __name__=='__main__':
    pool=Pool()
    page=([x for x in range(1,601)])

    pool.map(main,page)
    pool.close()
    pool.join()



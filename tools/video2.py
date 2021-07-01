import requests
from lxml import etree
from multiprocessing.dummy import Pool as pl
import csv
import time
import json

def towrite(item):
    with open('video3.csv','a',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        try:
            writer.writerow(item)
        except:
            print('write Error!')
def spilder(url):
    htm=requests.get(url,headers=headers)
    response=etree.HTML(htm.text)

if __name__=='__main__':
    pool=pl(4)
    start_url="https://www.ximalaya.com/search/"
    poem_names=[]
    # 使用readline()读文件
    f = open("poem2.txt", encoding='utf-8')
    while True:
        line = f.readline()
        if line:
            # print(line)
            poem_names.append(line)
        else:
            break
    # print(poem_names)
    # print(poem_names[0])
    f.close()
    print(poem_names)
#     poem_names=[
#         "行路难·其二李白","喜春来·七夕","大德歌·秋","水调歌头·赋三门津","人月圆·吴门怀古",
# "九辩","塞鸿秋·代人作","蟾宫曲·咏西湖","招魂作者屈原","普天乐·雨儿飘"]
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36"
    }
    all_url=[]
    for name in poem_names:
        name=name.replace('\n','')
        url=start_url+name
        print("---")
        # print(url)
        print(url)
        htm=requests.get(url,headers=headers)
        # print(htm.text)
        selector=etree.HTML(htm.text)
        print(selector)
        url_tail=selector.xpath("//*[@id='searchPage']/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[5]/div/div/h4/a/@href")
        all_url=[]
        if url_tail:
            url_tail = selector.xpath("//*[@id='searchPage']/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[5]/div/div/h4/a/@href")[0]
            id=url_tail.split("/")[3]
            url1="https://www.ximalaya.com"+url_tail
            print("url1===",url1)
            # htm1=requests.get(url1,headers)


            url_vedio="https://www.ximalaya.com/revision/play/v1/audio?id="+id+"&ptype=1"
            # url_vedio="https://www.ximalaya.com/revision/play/v1/audio?id=149892904&ptype=1"
            print("url==",url_vedio)
            print("name===",name)
            all_url.append(url_vedio)
            response = requests.get(url_vedio, headers=headers)
            result = response.text
            result = json.loads(result)
            src=result['data']['src']
            print("src===",src)
            print(result)
            poem_item=[name,src]
            towrite(poem_item)

    pool.map(spilder,all_url)
    pool.close()
    pool.join()
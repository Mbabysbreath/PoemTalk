import requests
from lxml import etree
import csv
# 导入线程池
from multiprocessing.dummy import Pool as pl
import urllib

def towrite(item):
    with open('poet_info4.csv','a',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        try:
            writer.writerow(item)
        except:
            print('write Error!')
def spilder(url):

    for num in range(1,11):
        # "https://so.gushiwen.cn/authors/Default.aspx?p=1&c=%e5%85%88%e7%a7%a6"
        start_url = url.split('p=')[0]+"p="+str(num)+"&c="+url.split('c=')[1]
        htm = requests.get(start_url,headers=headers)
        htm.encoding="utf-8"
        response = etree.HTML(htm.text)
        poet_list = response.xpath("//*[@id='leftZhankai']/div")
        # poet_list = response.xpath("//*[@id="leftZhankai"]/div[2]")
        url=str(url)
        for poet in poet_list:
            name = poet.xpath("div[1]/p[1]/a[1]/b/text()")
            if name:
                name=poet.xpath("div[1]/p[1]/a[1]/b/text()")[0]

            # name = poet.xpath("//*[@id="leftZhankai"]/div[12]/div[1]/p[1]/a[1]/b")[0]


            img = poet.xpath("div[1]/div/a/img/@alt")
            if img:
                img = poet.xpath("div[1]/div/a/img/@alt")[0]
                # img = poet.xpath("div[1]/div/a/img/@src")[0]
                # img = poet.xpath("//*[@id="leftZhankai"]/div[2]/div[1]/div/a/img")[0]

                print("图片地址",img)
                img = 'poet/' + img + '.jpg'
            else:
                img='poet/logo-1.jpg'
            img_url = poet.xpath("div[1]/div/a/img/@src")
            # img_url = poet.xpath("div[1]/div/a/img/@src")
            if img_url:
                img_url = poet.xpath("div[1]/div/a/img/@src")[0]
                b_img=requests.get(img_url,headers=headers)
                # with open('D:\codeZM\PoemTalk\static\media\poet/'+name+'.jpg','wb') as tp:
                #     tp.write(b_img.content)
            dynasty = url.split('c=')[1]
            dynasty=urllib.request.unquote(dynasty)
            print("朝代==",dynasty)
            desc = poet.xpath("div[1]/p[2]/text()")
            if desc:
                desc = poet.xpath("div[1]/p[2]/text()")[0]

            print("正在爬取",name)
            love_num=0
            if name and desc:
                poet_item=[img,name,dynasty,desc,love_num]
                towrite(poet_item)
# 1.作者：头像、姓名、生平事迹、朝代、简述
if __name__ == '__main__':

    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36"
    }
    start_url="https://so.gushiwen.cn/authors/"
    pool = pl(4)
    all_url=[]
    html = requests.get(start_url, headers=headers)
    selector = etree.HTML(html.text)
    for num in range(1,13):
        path = "//*[@id='html']/body/div[2]/div[1]/div[1]/div[2]/div[2]/a["+str(num)+"]/@href"

        print("path==",path)
        dynasty_url = selector.xpath(path)[0]
        # dynasty_url = selector.xpath("//*[@id='html']/body/div[2]/div[1]/div[1]/div[2]/div[2]/a[2]")[0]
        print(num,'==',dynasty_url)
        dynasty_url= "https://so.gushiwen.cn/"+dynasty_url
        all_url.append(dynasty_url)
    pool.map(spilder, all_url)
    pool.close()
    pool.join()






import requests
from lxml import etree
from multiprocessing.dummy import Pool as pl
import csv
import time
def towrite(item):
    with open('video.csv','a',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        try:
            writer.writerow(item)
        except:
            print('write Error!')
def spilder(url):
    htm = requests.get(url,headers=headers)
    # print(htm.te)
    response = etree.HTML(htm.text)
    title = response.xpath("//*[@id='sonsyuanwen']/div[1]/h1/text()")
    if title:
        title = response.xpath("//*[@id='sonsyuanwen']/div[1]/h1/text()")[0]
    else:
        title=''
    author = response.xpath("//*[@id='sonsyuanwen']/div[1]/p/a[1]/text()")
    if author:
        author = response.xpath("//*[@id='sonsyuanwen']/div[1]/p/a[1]/text()")[0]
        print('作者-1：', author)
    else:
        author = ""
    poemtype_id = 1
    poetinfo_id = 1
    dynastys=['〔唐代〕','〔宋代〕','〔先秦〕','〔两汉〕','〔元代〕','〔清代〕','〔明代〕','〔金朝〕','〔魏晋〕','〔南北朝〕','〔五代〕','〔隋代〕']
    dynasty = response.xpath("//*[@id='sonsyuanwen']/div[1]/p/a[2]/text()")
    # author = response.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/p[2]/a[1]")
    if dynasty:
        dynasty = response.xpath("//*[@id='sonsyuanwen']/div[1]/p/a[2]/text()")[0]
        if dynasty=='〔先秦〕' and author=='佚名':#诗经
            poemtype_id=4
        else:
            poemtype_id=3 #楚辞
        if dynasty=='〔唐代〕':
            poemtype_id=1
        if dynasty=='〔宋代〕':
            poemtype_id=2
        if dynasty=='〔两汉〕':
            poemtype_id=3
        if dynasty=='〔元代〕':
            poemtype_id=11
        if dynasty=='〔清代〕':
            poemtype_id=5
        if dynasty=='〔明代〕':
            poemtype_id=6
        if dynasty=='〔金朝〕':
            poemtype_id=7
        if dynasty=='〔魏晋〕' or dynasty=='〔南北朝〕':
            poemtype_id=8
        if dynasty=='〔五代〕':
            poemtype_id=9
        if dynasty=='〔隋代〕':
            poemtype_id=10

    else:
        dynasty="hhhhh"

    print("dynasty==",dynasty)
    contents = response.xpath("//*[@id='sonsyuanwen']/div[1]/div[2]/p/text()")

    if contents:
        contents = response.xpath("//*[@id='sonsyuanwen']/div[1]/div[2]/p/text()")
    else:
        contents = response.xpath("//*[@id='sonsyuanwen']/div[1]/div[2]/text()")
    # contents = response.xpath("//*[@id='sonsyuanwen']/div[1]/")
    content=""
    for item in contents:
        content+=item
        content+='\n'
    translations = response.xpath("//*[@id='html']/body/div[2]/div[1]/div[3]/div[1]/p[1]/text()")
    if translations:
        translations = response.xpath("//*[@id='html']/body/div[2]/div[1]/div[3]/div[1]/p[1]/text()")
        print('翻译-1',translations)
    else:

        translations = response.xpath("//*[@id='html']/body/div[2]/div[1]/div[4]/div[1]/p[1]/text()")
        print('翻译-2',translations)

    translation=""
    for item in translations:
        translation = translation + item + "\n"
    notes = response.xpath("//*[@id='html']/body/div[2]/div[1]/div[3]/div[1]/p[2]/text()")

    if notes:
        notes = response.xpath("//*[@id='html']/body/div[2]/div[1]/div[3]/div[1]/p[2]/text()")
        print("注释-1：",notes)
    else:
        notes = response.xpath("//*[@id='fanyiquan845']/div[1]/p[2]/text()")
        print("注释-2：",notes)

    note=""
    for item in notes:
        note = note + item + '\n'
    print("注释：", note)
    video_url = response.xpath("/html/body/div[2]/div[1]/div[2]/div[3]/@id")
    # video_url = response.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[3]/div/audio/@id")
    if video_url:
        video_url = response.xpath("/html/body/div[2]/div[1]/div[2]/div[3]/@id")[0]
        id=video_url.replace("toolPlay","")
        print("id=",id)
        video_url = "https://so.gushiwen.cn/viewplay.aspx?id=" + id

        htm1 = requests.get(video_url, headers=headers)
        response = etree.HTML(htm1.text)
        video_url = response.xpath("/html/body/div[1]/audio/@src")[0]

        print("mp3==",video_url)
    else:
        video_url='mp3'
    print("uuuuu", video_url)
    love_num = 0
    study_num=0
    click_num = 0
    add_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(add_time)
    poem_item=[title,content,author,video_url]
    # poem_item=[title,content,author,translation,note,video_url,love_num,study_num,click_num,add_time,poemtype_id,poetinfo_id]
    towrite(poem_item)

if __name__ == '__main__':
    pool = pl(4)
    start_url ="https://so.gushiwen.cn/gushi/"
    start_url_dynasty="https://so.gushiwen.cn/shiwens/default.aspx?cstr="
    poem_kinds = ["tangshi.aspx","shijing.aspx","songsan.aspx","yuefu.aspx","chuci.aspx","default.aspx?xstr=曲"]
    poem_kinds_dynasty = ["魏晋","南北朝","隋代","五代","金朝","明代","清代"]
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36"
    }
    all_url = []
    for poem_url_tail in poem_kinds:
        if poem_url_tail == "default.aspx?xstr=曲":
            url ="https://so.gushiwen.cn/shiwens/default.aspx?xstr=%e6%9b%b2"
        else:
            url = start_url+poem_url_tail
        # print(url)
        htm = requests.get(url,headers=headers)
        selector = etree.HTML(htm.text)
        poem_list = selector.xpath("//*[@id='html']/body/div[2]/div[1]/div/div/span/a/@href")
        for poem in poem_list:
            poem_url = "https://so.gushiwen.cn/"+poem
            # video=selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[3]/div/audio/@src")
            # video=selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[3]/div/audio/@controls")
            # print("video--------",video)
            all_url.append(poem_url)
    for poem_url_tail in poem_kinds_dynasty:
        url = start_url_dynasty + poem_url_tail
        htm = requests.get(url, headers=headers)
        selector = etree.HTML(htm.text)

        # poem_list = selector.xpath("//*[@id='html']/body/div[2]/div[1]/div/div/span/a/@href")
        # poem_list = selector.xpath("//*[@id='html']/body/div[2]/div[1]/div/div/span/a/@href")
        poem_list = selector.xpath("//*[@id='leftZhankai']/div")
        # poem_list = selector.xpath("//*[@id="html"]/body/div[2]/div[1]/div[2]/div[1]/span[1]/a")
        # poem_list = selector.xpath("/html/body/div[2]/div[1]/div[2]/div[1]/span[1]/a")
        # poem_list = selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/p[1]/a")
        for poem in poem_list:
            url=poem.xpath("div[1]/p[1]/a/@href")
            if url:
                url = poem.xpath("div[1]/p[1]/a/@href")[0]
                poem_url = "https://so.gushiwen.cn/" + url
                print(poem_url)
                all_url.append(poem_url)


    pool.map(spilder, all_url)
    pool.close()
    pool.join()




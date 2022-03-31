import pandas as pd
import requests
from lxml import etree
from urllib import parse
import time

Universities = pd.read_excel("211大学名单.xlsx")
# 可更改查询专业代号
code = '0854'
for University_ch in Universities['院校']:
    chi= []
    University = parse.quote(University_ch)
    url = 'https://yz.chsi.com.cn/zsml/querySchAction.do?dwmc=' + University \
          +'&mldm=zyxw&mlmc=&yjxkdm='+ code +'&xxfs=&zymc='
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'
    }
    rep1 = requests.get(url=url,headers=ua)
    rep_xpath = etree.HTML(rep1.text)
    uni_211s = rep_xpath.xpath('/html/body//table//a/@href')
    index = 0
    for uni_211 in uni_211s:
        url2 = 'https://yz.chsi.com.cn'+uni_211

        rep_uni = requests.get(url=url2,headers=ua)
        rep_uni.encoding = 'utf-8'
        rep_uni = etree.HTML(rep_uni.text)
        course = rep_uni.xpath('//tbody//td[4]/text()')
        chi.append(course[2:5])
        print(index)
        index += 1
        time.sleep(0.5)  # 不要攻击服务器 休息一下
    pd.DataFrame(chi).to_excel('./data/'+ University_ch + '.xlsx',sheet_name='Sheet1', index=False)
    print('%s爬取结束' % University_ch)


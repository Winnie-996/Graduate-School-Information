import requests
from lxml import etree
from urllib import parse
import time

def OutputInfo(University_ch,code):
    print('%s--%s--招生信息: '%(University_ch,code))
    print('专业方向'+' '*20+'招生人数' + ' ' * 20+'专业课')
    chi= []
    University = parse.quote(University_ch)
    url = 'https://yz.chsi.com.cn/zsml/querySchAction.do?dwmc=' + University +'&mldm=zyxw&mlmc=&yjxkdm='+str(code)+'&xxfs=&zymc='
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
        print('{0: <20}{1: <20}{2: <20}'.format(course[2],course[3],course[4]))
        time.sleep(0.5)  # 不要攻击服务器 休息一下

if __name__ == '__main__':
    University_ch = input('输入查询院校：')
    code = input('输入查询专业代号：')
    OutputInfo(University_ch,code)
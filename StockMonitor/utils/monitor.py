# import random
#
# a = random.choice(["张家界","长白山",'格林美',"木林森"])
# print(a)
import time
import requests   # 爬虫库
import datetime
from chinese_calendar import is_holiday
from .dingding import send_msg

"""
0：”大秦铁路”，股票名字；
1：”27.55″，今日开盘价；
2：”27.25″，昨日收盘价；
3：”26.91″，当前价格；
4：”27.55″，今日最高价；
5：”26.20″，今日最低价；
6：”26.91″，竞买价，即“买一”报价；
7：”26.92″，竞卖价，即“卖一”报价；
8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
10：”4695″，“买一”申请4695股，即47手；
11：”26.91″，“买一”报价；
12：”57590″，“买二”
13：”26.90″，“买二”
14：”14700″，“买三”
15：”26.89″，“买三”
16：”14300″，“买四”
17：”26.88″，“买四”
18：”15100″，“买五”
19：”26.87″，“买五”
20：”3100″，“卖一”申报3100股，即31手；
21：”26.92″，“卖一”报价
(22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况”
30：”2008-01-11″，日期；
31：”15:05:32″，时间；
"""

"""在大范围爬取之前,很有必要先尝试一个小demo,测试一下所想和取得的是否对应
为了更全面测试这里分多种情况,正常股票sh600000退市股票：sh600002停牌股票：sz300124，除权股票：sh600276，上市新股：sz002952"""

max_proportion = 2
min_proportion = -2
stock_code_list = ["sz000831", "sh603993", "sh605376"]
url = "http://hq.sinajs.cn/list="+",".join(stock_code_list)
headers = {"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
           " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 			 Safari/537.36"}


def is_runtime():
    date = datetime.datetime.now().date()
    if is_holiday(date):
        return False
    # 范围时间
    am_start_time = datetime.datetime.strptime(str(date) + '9:30', '%Y-%m-%d%H:%M')
    am_end_time = datetime.datetime.strptime(str(date) + '11:30', '%Y-%m-%d%H:%M')
    pm_start_time = datetime.datetime.strptime(str(date) + '13:00', '%Y-%m-%d%H:%M')
    pm_end_time1 = datetime.datetime.strptime(str(date) + '15:00', '%Y-%m-%d%H:%M')
    # 当前时间
    n_time = datetime.datetime.now()
    return am_start_time < n_time < am_end_time or pm_start_time < n_time < pm_end_time1

# 设置请求头

def handle(self, *args, **options):
    if not is_runtime():
        return
    response = requests.get(url).text # 获取的文本内容
    content = response.strip()  # 把前后空白字符去除一下
    data_line = content.split("\n")
    data = [i.replace("var hq_str_"," ").split(",") for i in data_line]
    data_list = []
    for key in data:
        proportion = (float(key[3]) / float(key[2]) - 1) * 100
        if min_proportion < proportion < max_proportion:
            return
        proportion = ("%.2f" % proportion) + "%"
        data_list.append(dict(name=key[0].strip().replace('="', '-'),
                price=key[3],
                max_price=key[4],
                min_price=key[5],
                proportion=proportion,
                current_time=key[30]+" "+key[31],
                )
        )
    if data_list:
        send_msg(data_list)

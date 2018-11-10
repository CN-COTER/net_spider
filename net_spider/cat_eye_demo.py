# coding:utf-8
#
import requests
import re
import json

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def write_tofile(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')

def main(offset):
    url = 'https://maoyan.com/board/4/?offset=' + str(offset)

    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_tofile(item)


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '排名': item[0],
            # 'image': item[1],
            '电影名': item[2],
            '演员': item[3].strip()[3:],
            '上映时间': item[4].strip()[5:],
            '评分': item[5] + item[6]
        }


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)

import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool
import re, json, demjson


headers = {
    # 'Host': 'm.weibo.cn',
    # 'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def get_page(offset):
    param = {
        "aid": 24,
        "app_name": "web_search",
        "offset" : offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': 1,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    url = 'http://www.toutiao.com/api/search/content/?' + urlencode(param)
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.json()
    except BaseException as e:
        print(e)
        return None

def get_article(data_json):
    if data_json.get('data'):
        for item in data_json.get('data'):
            if item.get('abstract'):
                url = item.get('article_url')
                if 'toutiao.com' in url:
                    page_code = item.get('article_url').split('/')[-2]
                    url = 'https://www.toutiao.com/a' + page_code
                    yield{
                        'article_url': url
                    }


def jsonfy(s:str)->object:
    #此函数将不带双引号的json的key标准化
    obj = eval(s, type('js', (dict,), dict(__getitem__=lambda s, n: n))())


def get_html(url):
    try:
        html = requests.get(url, headers).text;
        # with open('jiepaihtml.txt', 'a', encoding=('utf-8')) as f:
        #     f.write(html + '\n')
        #     f.write('\n' + '=' * 50 + '\n')
        pattern = re.compile("articleInfo:.*?(.*?);</script>", re.S)
        items = re.findall(pattern, html)
        if items:
            result = items[0]
            return result
        else:
            return None
    except BaseException as e:
        print(e)
        return None

def parse_json(html):
    try:
        if html:
            pattern = re.compile("pgc-img&quot;.*?&quot;(.*?)&quot;", re.S)
            #print(title)
            items = re.findall(pattern, html)
            i = 0 
            for item in items:
                i += 1
                yield{
                    'title': i,
                    'url': item
                }
    except BaseException as e:
        print(e)

def save_image(item):
    title = item.get("title")
    title = "img" + str(title)
    if not os.path.exists(title):
        os.mkdir(title)
    try:
        response = requests.get(item.get('url'))
        if response.status_code == 200:
            file_path = os.path.join(title, '{0}.{1}'.format(md5(response.content).hexdigest(), 'jpg'))
            #print(file_path)
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Falied to Save Image')


def main(offset):
    page_jsons = get_page(offset)
    for article_url in get_article(page_jsons):
        content_json = get_html(article_url.get('article_url'))
        for item in parse_json(content_json):
            save_image(item)

GROUP_START = 0
GROUP_END = 10

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END)])
    pool.map(main, groups)
    pool.close()
    pool.join()

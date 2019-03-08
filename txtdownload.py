from lxml import etree
import requests, re


headers = {
    'Host': 'www.biquge.cc',
    # 'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    #'X-Requested-With': 'XMLHttpRequest',
}

main_url = 'https://www.biquge.cc/html/54/54656/'
#url = 'https://www.baidu.com'
book_name="article"

def get_page_url(url):
    try:
        text = requests.get(url, headers = headers, verify = False).text
        pattern = re.compile("</dd>.*?<dt>(.*?)</dt>(.*?)</dl>", re.S)
        items = re.findall(pattern, text)
        for item in items:
            title = item[0]
            book_name = title +'.txt'
            with open(book_name, 'a', encoding='utf-8') as f:
                f.write(title + '\n')
            return item[1]
    except Exception as e:
        print(e)
    
def parse_html(html):
    html = etree.HTML(html)
    items = html.xpath('//dd');
    for item in items:
        page_title = item.xpath('.//a/text()')
        url = item.xpath('.//a/@href')
        yield{
            'title': "".join(page_title),
            'url': main_url + "".join(url)
        }

def get_content(item):
    title = item.get('title')
    page_url = item.get('url')
    text = requests.get(page_url, headers = headers, verify = False).text
    html = etree.HTML(text)
    content = html.xpath("//div[@id='content']/text()")
    content = "".join(content);
    content = content.replace("\xa0\xa0\xa0\xa0", '\n')
    content = content.replace("<br />", '\n')
    with open(book_name, 'a', encoding='utf-8') as f:
        f.write(title + '\n')
        f.write(content)

    
if __name__ == '__main__':
    #get_page_url(main_url)
    #get_content('https://www.biquge.cc/html/54/54656/5611298.html')
    html = get_page_url(main_url)
    items = parse_html(html)
    for item in items:
        get_content(item)


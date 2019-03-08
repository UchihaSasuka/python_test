from bs4 import BeautifulSoup


# soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# print(soup.p.string)
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b name="23123">The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())
# print(soup.title.string)
# print(type(soup.title))
# print(soup.title)
# print(soup.head)
# print(soup.p['name'])
# print(soup.p['class'][0])
# print(soup.p.contents)
# for i, child in enumerate(soup.p.children):
#     print(i, child)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)
# print(soup.a.parent)
#print(list(enumerate(soup.a.parents)))

# print(soup.a.next_sibling)
# print(soup.a.previous_sibling)
#print(list(soup.p.children)[0]['name'])


#find_all(name, attrs, recursive, text, **kwargs)

# print(soup.find_all(name='url'))
# print(type(soup.find_all(name='ul')[0]))
#import re
# print(soup.find_all(attrs={'id':'list-1'}))
#print(soup.find_all(name = 'li', text = re.compile('Foo')))

# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
#print(soup.select('ul'))

# for ul in soup.select('ul'):
#     print(ul.select('li'))

# import requests
# from pyquery import PyQuery as pq

# url = 'https://www.zhihu.com/explore'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
# html = requests.get(url, headers=headers).text
# with open('zhihu.txt', 'a', encoding='utf-8') as f:
#     f.write(html)
# doc = pq(html)
# items = doc('.explore-tab .feed-item').items()
# for item in items:
#     question = item.find('h2').text()
#     author = item.find('.author-link-line').text()
#     answer = pq(item.find('.content').html()).text()
#     with open('explore.txt', 'a', encoding='utf-8') as f:
#         f.write('\n'.join([question, author, answer]))
#         f.write('\n' + '=' * 50 + '\n')


# import json
 
# str = '''
# [{
#     "name": "李鹏",
#     "gender": "男",
#     "birthday": "1992-10-18"
# }, {
#     "name": "Selina",
#     "gender": "female",
#     "birthday": "1995-10-18"
# }]
# '''
# print(type(str))
# data = json.loads(str)
# print(data)
# print(type(data))

# with open('data.json', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(data, indent=2, ensure_ascii=False))

import csv
 
with open('data.csv', 'w') as csvfile:
    # writer = csv.writer(csvfile)
    # writer.writerow(['id', 'name', 'age'])
    # writer.writerow(['10001', 'Mike', 20])
    # writer.writerow(['10002', 'Bob', 22])
    # writer.writerow(['10003', 'Jordan', 21])
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001', 'name':'Mike', 'age':20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)






































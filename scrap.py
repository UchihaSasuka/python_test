# import urllib.request
# import urllib.parse
# import urllib.error
# import socket
# from urllib import request, parse
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
# import http.cookiejar
# from urllib.parse import urlparse
# from urllib.parse import urlunparse
# from urllib.parse import urljoin
#response = urllib.request.urlopen("http://www.python.org")
#print(response.read().decode("utf-8"))
#print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding = 'utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout= 0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('Time out')

# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf8'))

# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent':'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name':'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# proxy_handler = ProxyHandler({
#     'http':'http://127.0.0.1:9743',
#     'https':'http://127.0.0.1:9734'
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(resopnse.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)
# cookie = http.cookiejar.CookieJar()
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)
# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)
# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result),result)

# result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
# print(result)

# result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
# print(result)

# data= ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))
#后面的url弥补前面缺失的部分
# print(urljoin('http://www.baidu.com', 'FAQ.html'))     
import requests
 
# r = requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)
# data = {
#     'name' : 'germey',
#     'age' : 22
# }
# r = requests.get("http://httpbin.org/get", params=data)
# print(r.text)

# import re
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)
# r = requests.get("http://github.com/favicon.ico")
# with open('favicon.ico','wb') as f:
#     f.write(r.content)
# data = {'name':'germey', 'age':22}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)

r = requests.get("https://www.jianshu.com", headers=headers)
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)
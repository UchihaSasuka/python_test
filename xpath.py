from lxml import etree
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
text = '''
<dd> <a style="" href="5611401.html">第六卷 天道卷 后记</a></dd>
'''
html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))
#html = etree.parse('./test.html', etree.HTMLParser())
#result = html.xpath('//*')
#result = html.xpath('//li')
#result = html.xpath('//li/a')

#result = html.xpath('//li[@class="item-0"]/text()')
#result = html.xpath('//li[@class="item-0"]//text()')
#result = html.xpath('//li[@class="item-0"]/a/text()')
# result = html.xpath('//li[1]/a/@href')
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')

results = html.xpath('//dd')
for item in results:
    print(item.xpath('//a/@href'))
#print(etree.tostring(result, encoding = 'utf-8'))
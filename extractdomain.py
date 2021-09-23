def domain_name(url):
    url = url.replace('http://','').replace('https://','').replace('http://www.','').replace('https://www.','').replace('www.','')
    url = url.split('.')
    return url[0]



x = "http://google.com"
x2 = "http://google.co.jp"
x3 = "www.xakep.ru"
x4 = "https://youtube.com"
print(domain_name(x4)(x3))
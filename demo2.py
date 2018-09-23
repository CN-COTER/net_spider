#利用handler的几个实例；

#实例1：验证
# 实例化HTTPBasicAuthHandler对象，添加url,username,passord创建一个处理验证的Handler
# from urllib.request import HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm,build_opener
# from urllib.error import URLError
# username = 'username'
# password = 'password'
# url ='http://localhost:5000/'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

#实例2：代理
#在本地搭建代理，运行在9743端口上，使用ProxyHandler()参数是一个字典，键是协议类型（http/https）,值是代理链接，可添加多个代理。

# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)
#

#实例3：Cookies
#声明一个CookJar,利用HTTPCookieProcessor构建一个Handler
import http.cookiejar
import urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
# print(cookie)
# for item in cookie:
#     print(item.name+'='+item.value)


#实例4：




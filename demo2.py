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
#     # 'https': 'https://127.0.0.1:9743'     只需要设置一个代理地址
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)


#实例3：Cookies
#声明一个CookJar,利用HTTPCookieProcessor构建一个Handler
# import http.cookiejar
# import urllib.request
# filename = 'cookies.txt'
# # cookie = http.cookiejar.CookieJar()
# # cookie = http.cookiejar.MozillaCookieJar(filename)      #MozillaCookieJar用于处理Cookies和文件相关的事件
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

#使用本地的cookies文件（必须是LWPCookieJar格式的Cookies）
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# print(response.read().decode('utf8'))



#实例4：处理异常:URLError,HTTPError(子类)[code,reason,headers]
# from urllib import request, error
# try:
#     response = request.urlopen(' https://cuiqingcai.com/index.htm', timeout=0.1)
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers)


#先输出子异常再输出父异常

# from urllib import request, error
# try:
#     response = request.urlopen(' https://cuiqingcai.com/index.htm', timeout=0.1)
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers)
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

#异常reason返回的是一个对象
import socket
from urllib import request, error
try:
    response = request.urlopen(' https://www.baidu.com', timeout=0.01)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')





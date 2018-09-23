# urllib 4 模块:request(模拟发送http请求，给库方法传入url和参数即可)
import urllib.request
import urllib.parse
import socket
import urllib.error

# response = urllib.request.urlopen('https://www.baidu.com')  #urlopen:最基本的构造http请求的方法
# print(response.read().decode('utf-8'))
# print(response.getheaders())
# print("____________________________________")



# print(response.getheader('server'))     #响应中的server值
# print(response.status, response.msg, response.version, response.reason, response.debuglevel, response.closed)


# 模拟post请求加入参数，进行表单提交。
data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf8')      #字节流编码格式需要用bytes()方法来转化
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())


# timeout参数的使用
# try:
#     response1 = urllib.request.urlopen('http://httpbin.org', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('Time Out')



print('000000000000000000000000000000000000000000000000000000000000')
#Request    通过创建request对象并且对其进行设置
# request = urllib.request.Request('http://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

print('！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')


from urllib import parse, request
url = 'http://python.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'Host': 'httpbin.org'
}
dict1 = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict1), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers,  method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))










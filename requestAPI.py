#encoding:utf-8
import unittest
import requests
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    """"""
    @data("13962663") #数据驱动
    def test_resquest(self,userid):

        url="http://mobile.jingwei.com/getgroup"

        body={"userId":userid,"token":"278749575f90ab842327b294e4ad38b8"}

        response=requests.get(url,body) #打开一个接口

        print '\n'+'>>>>>> headers >>>>>>>>'
        print response.headers #获取返回的头信息

        print '\n' + '>>>>>> request headers >>>>>>>>'
        print response.request.headers  # 返回request的header

        print '\n'+'>>>>>> content-type >>>>>>>>'
        print response.headers['content-type'] #返回header中content－type的值

        print '\n'+'>>>>>> content-type >>>>>>>>'
        print response.headers.get('content-type') #返回header中content－type的值

        print '\n'+'>>>>>> encoding >>>>>>>>'
        print response.encoding #返回编码方式

        print '\n'+'>>>>>> text >>>>>>>>'
        print response.text #获取返回的response中data的值

        print '\n'+'>>>>>> content >>>>>>>>'
        print response.content #获取返回的response中data的值

        print '\n'+'>>>>>> json headers >>>>>>>>'
        print response.json() #将response值转换成unincode格式

        print '\n'+'>>>>>> status code >>>>>>>>'
        print response.status_code #获取返回的状态码

        print '\n'+'>>>>>> status code name >>>>>>>>'
        print response.reason #获取状态码的含义

        print '\n'+'>>>>>> history >>>>>>>>'
        print response.history #追踪重定向

        print '\n'+'>>>>>> exception  >>>>>>>>'
        response.raise_for_status() #如果请求错误(一个 4XX 客户端错误，或者 5XX 服务器错误响应),抛出异常

        self.assertTrue(u"合作" in response.text) #判断"合作"是否在response值中

    def test_request_type(self):
        """http 请求类型"""

        r = requests.get('https://github.com/timeline.json') #get请求

        r = requests.post("http://httpbin.org/post") #post请求

        r = requests.put("http://httpbin.org/put") #put请求

        r = requests.delete("http://httpbin.org/delete") #delete请求

        r = requests.head("http://httpbin.org/get") #head请求

        r = requests.options("http://httpbin.org/get") #option请求

    def test_request_params(self):
        """请求参数带参数情况"""

        # 用allow_redirects 参数设定重定向，False为否，True反之
        r = requests.get('http://github.com', allow_redirects=False)

        payload = {'key1': 'value1', 'key2': ['value2', 'value3']}  # get请求参数
        r = requests.get('https://github.com/timeline.json', params=payload)  # 带参数的get请求
        print(r.url)  # 打印url
        # 输出结果为：http://httpbin.org/get?key1=value1&key2=value2&key2=value3

        payload = {'key1': 'value1', 'key2': 'value2'}  # post请求参数
        r = requests.post("http://httpbin.org/post", data=payload)  # 带参数的post请求

        #requests.get('http://github.com', timeout=0.001) #告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应


if __name__ == '__main__':
    test=MyTestCase()
    test.test_resquest
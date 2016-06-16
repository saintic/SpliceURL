# SpliceURL
Splice, Split and Modify URL's python package

# Usage:

```
    一、安装
    #pip install SpliceURL

    二、使用
    """
    1、第一个参数必须是域名,domain=?;
    2、第二个参数是域名协议,scheme=?,默认是http;
    3、第三个参数是路径,path=?,默认是/;
    4、第四个参数是参数,params=?,默认是None;
    5、第五个参数是查询,query=?,默认是None,可传入字符串(如user=xxx&passwd=xxx)或字典(如{"user": "xxxx", "passwd": ""xxxx"});
    6、第六个参数是段位,fragment=?,默认是None.
    Everything is ok, now run do().
    """

    >>> s=SpliceURL.Splice(domain='saintic.com')
    >>> s.do()
    'http://saintic.com/'

    >>> SpliceURL.Splice(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}).do()
    'http://saintic.com/?username=tcw&password=xxx&id=True'

    >>> SpliceURL.Splice('saintic.com', "https", "api/blog", '', 'api=true&token=true', '20').do()
    'https://saintic.com/api/blog?api=true&token=true#20'

    可以参考demo.py
```

#!/usr/bin/env python
#-*- coding:utf-8 -*-

__doc__     = "Splice, Split and Modify URL"
__date__    = '2016-09-20'
__author__  = "Mr.tao <staugur@saintic.com>"
__version__ = '0.6'
__license__ = 'MIT'

import re
import urllib
import urlparse

class SpliceException(Exception):
    pass

class ArgError(SpliceException):
    pass

class Splice(object):
    """拼接URL，传参要求
    1、第一个参数必须是域名,domain=?;
    2、第二个参数是域名协议,scheme=?,默认是http;
    3、第三个参数是路径,path=?,默认是/;
    4、第四个参数是参数,params=?,默认是None;
    5、第五个参数是查询,query=?,默认是None,可传入字符串(如user=xxx&passwd=xxx)或字典(如{"user": "xxxx", "passwd": ""xxxx"});
    6、第六个参数是段位,fragment=?,默认是None.

    Everything is ok, now run do().
    """

    def __init__(self, domain=None, scheme='http', path='/', params=None, query=None, fragment=None, **kw):
        """ 
        >>> s=SpliceURL.Splice(domain='saintic.com')
        >>> s.do()
        'http://saintic.com/'

        >>> SpliceURL.Splice(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}).do()
        'http://saintic.com/?username=tcw&password=xxx&id=True'

        >>> SpliceURL.Splice('saintic.com', "https", "api/blog", '', 'api=true&token=true', '20').do()
        'https://saintic.com/api/blog?api=true&token=true#20'
        """
        _dn_pat = re.compile(r'([0-9a-zA-Z\_*\.*\-*]+).([a-zA-Z0-9\-*\_*\.*]+)\.([a-zA-Z]+$)')
        _ip_pat = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
        ip  = kw.get("ip")
        if scheme == "http":
            port = kw.get("port", 80)
        if scheme == "https":
            port = kw.get("port", 443)
        if domain and re.match(_dn_pat, domain) == None: raise ArgError("domain miss match!")
        if ip and re.match(_ip_pat, ip) == None: raise ArgError("ip miss match!")
        if port != None and not isinstance(port, int): raise TypeError("port only is integer.")
        if query != None and not isinstance(query, (str, dict)): raise TypeError("query only is string or dict.")

        if isinstance(query, dict):
            self.query = urllib.urlencode(query)
        else:
            self.query = query
        self.scheme = scheme
        if domain:
            if port == 80 and scheme == "http":
                self.uri = domain
            elif port == 443 and scheme == "https":
                self.uri = domain
            else:
                self.uri = "%s:%d" %(domain, port)
        else:
            if port == 80 and scheme == "http":
                self.uri = ip
            elif port == 443 and scheme == "https":
                self.uri = ip
            else:
                self.uri = "%s:%d"%(ip, port)
        self.path   = path
        self.params = params
        self.fragment = fragment

    def do(self):
        "run it, you can get a good stitching of the complete URL."
        return urlparse.urlunparse((self.scheme, self.uri, self.path, self.params, self.query, self.fragment))

    @property
    def geturl(self):
        "Equivalent class properties of the `do` function"
        return self.do()

    def __unicode__(self):
        return "Splice URL for SaintIC ULR Project."


class Split(object):
    """拆分URL，参数为url，返回元组，顺序为scheme,domain, path, params, query, fragment"""

    def __init__(self, url):
        """
        >>> import SpliceURL
        >>> Url = "https://www.saintic.com/auth?username=hello&password=wolrd"
        >>> print(SpliceURL.Split(Url).do())
        ('https', 'www.saintic.com', '/auth', '', 'username=hello&password=wolrd', '')
        """
        self.url = url

    def do(self):
        "run it, you can get a tuple for (scheme, domain, path, params, query, fragment)"
        _PR = urlparse.urlparse(self.url)
        return _PR.scheme, _PR.netloc, _PR.path, _PR.params, _PR.query, _PR.fragment

    def __unicode__(self):
        return "Split URL for SaintIC ULR Project."


class Modify(object):
    """修改URL，为ULR项目开设的组件，传入一个url和dict查询字典，组成成新url返回。
    典型的应用场景是Web应用接受登录注册请求访问ULR控制，操作完后跳转到新URL，这个新URL带有额外查询参数。
    """

    def __init__(self, url, **args):
        """
        >>> import SpliceURL
        >>> ReqUrl = "https://www.saintic.com/auth?username=hello&password=wolrd" #Accept a URL request, add the parameter and return!
        >>> AddArg = {"token": "abcdefghijklmnopqrstuvwxyz", "session": "F29243D66E9F50499AE5F3F873AE3516", "SignIn": True}
        >>> NewUrl = SpliceURL.Modify(ReqUrl, **AddArg).do()
        >>> print(NewUrl)
        https://www.saintic.com/auth?username=hello&password=wolrd&SignIn=True&token=abcdefghijklmnopqrstuvwxyz&session=F29243D66E9F50499AE5F3F873AE3516
        """
        if not isinstance(args, dict):
            raise TypeError("args ask a dict as query")
        self.url  = url
        self.args = args

    def do(self):
        "run it, get a new url"
        scheme, domain, path, params, query, fragment = Split(self.url).do()
        query += '&'
        query += urllib.urlencode(self.args)
        return Splice(scheme=scheme, domain=domain, path=path, params=params, query=query, fragment=fragment).do()

    @property
    def geturl(self):
        "Equivalent class properties of the `do` function"
        return self.do()

#!/usr/bin/env python
#-*- coding:utf-8 -*-

__doc__ = "Stitching generation URL"
__date__ = '2016-06-16'
__author__ = "Mr.tao <staugur@saintic.com>"
__version__ = '0.1'
__license__ = 'MIT'

import re
import urllib
import urlparse

class SpliceException(Exception):
    pass

class ArgError(SpliceException):
    pass

class SpliceURL(object):
    """拼接URL，传参要求
    1、第一个参数必须是域名,domain=?;
    2、第二个参数是域名协议,scheme=?,默认是http;
    3、第三个参数是路径,path=?,默认是/;
    4、第四个参数是参数,params=?,默认是None;
    5、第五个参数是查询,query=?,默认是None,可传入字符串(如user=xxx&passwd=xxx)或字典(如{"user": "xxxx", "passwd": ""xxxx"});
    6、第六个参数是段位,fragment=?,默认是None.

    Everything is ok, now run do().
    """

    def __init__(self, domain, scheme='http', path='/', params=None, query=None, fragment=None):
        """ 
        >>> s=SpliceURL.SpliceURL(domain='saintic.com')
        >>> s.do()
        'http://saintic.com/'

        >>> SpliceURL.SpliceURL(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}).do()
        'http://saintic.com/?username=tcw&password=xxx&id=True'

        >>> SpliceURL.SpliceURL('saintic.com', "https", "api/blog", '', 'api=true&token=true', '20').do()
        'https://saintic.com/api/blog?api=true&token=true#20'
        """

        if re.match(r'([0-9a-zA-Z\_*\.*\-*]+).([a-zA-Z0-9\-*\_*\.*]+)\.([a-zA-Z]+$)', domain) == None:
            raise ArgError("domain miss match!")
        if not isinstance(query, (str, dict)) and query != None:
            raise TypeError("query only is string or dict.")

        if isinstance(query, dict):
            self.query = urllib.urlencode(query)
        else:
            self.query = query
        self.scheme = scheme
        self.domain = domain
        self.path   = path
        self.params = params
        self.fragment = fragment

    def do(self):
        "run it, you can get a good stitching of the complete URL!"
        return urlparse.urlunparse((self.scheme, self.domain, self.path, self.params, self.query, self.fragment))

    def __unicode__(self):
        return "Splice URL for SaintIC ULR Project!"

    def __str__(self):
        return "Splice URL for SaintIC ULR Project!"

# SpliceURL
Splice, Split and Modify URL's python package

# Usage:

一、安装
```
pip install SpliceURL
```

二、使用
```
from SpliceURL import Splice, Split, Modify

print Splice(netloc='http://127.0.0.1', query={"username": "tcw", "password": "xxx", "id": True}).geturl
print Split("http://www.saintic.com/blog/?blogId=110&token=true&sso=false").do()
print Modify("http://www.saintic.com/blog", path='show/', query={"blogId": 115, "Token": "abcdefghjqmnoprstuvwxyz"}).geturl
```

# Note:
当前及之后版本(1.2)不向后兼容。

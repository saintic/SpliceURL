import SpliceURL
import unittest

version = SpliceURL.__version__

class SpliceTest(unittest.TestCase):

    def test_Splice(self):
        assert "http://saintic.com" in SpliceURL.Splice('saintic.com').do()
        assert "http://saintic.com/?username=tcw&password=xxx&id=True" in SpliceURL.Splice(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}).do()
        assert "http://saintic.com/api/user?username=tcw&password=xxx&id=True" in SpliceURL.Splice(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}, path="/api/user").do()
        assert "http://saintic.com" in SpliceURL.Splice(domain='saintic.com').do()
        SpliceURL.Splice(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}).do()
        assert "https://www.saintic.com/api/blog?username=tcw&password=xxx&id=True#20" in SpliceURL.Splice('www.saintic.com', 'https', "api/blog", '', 'username=tcw&password=xxx&id=True', '20').do()
        assert "https://saintic.com/blog#20" in SpliceURL.Splice('saintic.com', "https", "blog", '', '', '20').do()
        assert "http://api.com" in SpliceURL.Splice(ip="127.0.0.1", port=1001, domain="api.com").do()
        assert "http://127.0.0.1:10000" in SpliceURL.Splice(ip="127.0.0.1", port=10000).do()
        #print SpliceURL.Splice(ip="127.0.0.1", port=80).url
        assert "http://127.0.0.1:10000" in SpliceURL.Splice(ip="127.0.0.1", port=10000).geturl

    def test_Split(self):
        url='https://api.saintic.com/user?id=admin&time=true'
        s = SpliceURL.Split(url).do()
        self.assertEqual(type(s), tuple)
        assert "api.saintic.com" in s

    def test_Modify(self):
        ReqUrl = "https://www.saintic.com/auth?username=hello&password=wolrd"
        AddArg = {"token": "token", "session": "session", "SignIn": True}
        NewUrl = SpliceURL.Modify(ReqUrl, **AddArg).do()
        assert "token=token" in NewUrl
        assert "session=session" in NewUrl 
        assert "SignIn=True" in NewUrl

if __name__ == "__main__":
    unittest.main()

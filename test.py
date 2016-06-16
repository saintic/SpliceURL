import SpliceURL
import unittest

version = SpliceURL.__version__

class SpliceTest(unittest.TestCase):

    def test_Splice(self):
        assert "http://saintic.com" in SpliceURL.Splice(domain='saintic.com').do()
        
        assert "http://saintic.com/?username=tcw&password=xxx&id=True" in SpliceURL.Splice(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}).do()
        
        assert "http://saintic.com/api/user?username=tcw&password=xxx&id=True" in SpliceURL.Splice(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}, path="/api/user").do()
        
        assert "http://saintic.com" in SpliceURL.Splice('saintic.com').do()
        
        SpliceURL.Splice('saintic.com', query={"username": "tcw", "password": "xxx", "id": True}).do()
        
        assert "https://saintic.com/api/blog?username=tcw&password=xxx&id=True#20" in SpliceURL.Splice('saintic.com', "https", "api/blog", '', 'username=tcw&password=xxx&id=True', '20').do()

        assert "https://saintic.com/blog#20" in SpliceURL.Splice('saintic.com', "https", "blog", '', '', '20').do()

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

import SpliceURL
import unittest

class SpliceTest(unittest.TestCase):

    def test_Splice(self):
        assert "http://saintic.com:1000" in SpliceURL.Splice(netloc='saintic.com', port=1000).do()

    def test_Split(self):
        url='https://api.saintic.com/user?id=admin&time=true'
        s = SpliceURL.Split(url).do()
        self.assertEqual(type(s), tuple)
        assert "api.saintic.com" in s

    def test_Modify(self):
        ReqUrl = "https://www.saintic.com/auth?username=hello&password=wolrd"
        AddArg = {"token": "token", "session": "session", "SignIn": True}
        NewUrl = SpliceURL.Modify(ReqUrl, query=AddArg).geturl
        assert "token=token" in NewUrl
        assert "session=session" in NewUrl 
        assert "SignIn=True" in NewUrl

if __name__ == "__main__":
    unittest.main()

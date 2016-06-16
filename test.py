import SpliceURL
import unittest

version = SpliceURL.__version__

class SpliceTest(unittest.TestCase):

    def setUp(self):
        print "SpliceURL Version is", version

    def test_Splice(self):
        assert "http://saintic.com" in SpliceURL.SpliceURL(domain='saintic.com').do()
        
        assert "http://saintic.com/?username=tcw&password=xxx&id=True" in SpliceURL.SpliceURL(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}).do()
        
        assert "http://saintic.com/api/user?username=tcw&password=xxx&id=True" in SpliceURL.SpliceURL(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}, path="/api/user").do()
        
        assert "http://saintic.com" in SpliceURL.SpliceURL('saintic.com').do()
        
        SpliceURL.SpliceURL('saintic.com', query={"username": "tcw", "password": "xxx", "id": True}).do()
        
        assert "https://saintic.com/api/blog?username=tcw&password=xxx&id=True#20" in SpliceURL.SpliceURL('saintic.com', "https", "api/blog", '', 'username=tcw&password=xxx&id=True', '20').do()

        assert "https://saintic.com/blog#20" in SpliceURL.SpliceURL('saintic.com', "https", "blog", '', '', '20').do()

if __name__ == "__main__":
    unittest.main()

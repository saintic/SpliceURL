from SpliceURL import Splice, Split, Modify

if __name__ == "__main__":
    print Splice(netloc='http://127.0.0.1', query={"username": "tcw", "password": "xxx", "id": True}).geturl
    print Split("http://www.saintic.com/blog/?blogId=110&token=true&sso=false").do()
    print Modify("http://www.saintic.com/blog", path='show/', query={"blogId": 115, "Token": "abcdefghjqmnoprstuvwxyz"}).geturl

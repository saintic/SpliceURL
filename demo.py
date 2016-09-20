import SpliceURL

def splice():
    s=SpliceURL.Splice(domain='saintic.com')
    print(s.do())
    print(s.geturl)
    
    print(SpliceURL.Splice(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}).do())

    print(SpliceURL.Splice('saintic.com', "https", "api/blog", '', 'api=true&token=true', '20').do())

    print(SpliceURL.Splice(ip="127.0.0.1", scheme="https", port=550).do())
    print(SpliceURL.Splice(domain="saintic.com", port=80).geturl)

def split():
    Url = "https://www.saintic.com/auth?username=hello&password=wolrd"
    print(SpliceURL.Split(Url).do())

def modify():
    #Accept a URL request, add the parameter and return!
    ReqUrl = "https://www.saintic.com/auth?username=hello&password=wolrd"
    AddArg = {"token": "abcdefghijklmnopqrstuvwxyz", "session": "F29243D66E9F50499AE5F3F873AE3516", "SignIn": True}

    #NewUrl = SpliceURL.Modify(ReqUrl, **AddArg).do()
    NewUrl = SpliceURL.Modify(ReqUrl, **AddArg).geturl
    print(NewUrl)
    print(SpliceURL.Split(NewUrl).do())

if __name__ == "__main__":
    splice()
    split()
    modify()

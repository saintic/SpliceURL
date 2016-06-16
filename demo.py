import SpliceURL

url = SpliceURL.SpliceURL(domain='saintic.com')
print url.do()

print SpliceURL.SpliceURL(domain='saintic.com', query={"username": "tcw", "password": "xxx", "id": True}).do()

print SpliceURL.SpliceURL('saintic.com', "https", "blog", '', 'api=true&token=true', '20').do()

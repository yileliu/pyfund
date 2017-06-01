import urllib
import urllib2
import cookielib
import requests

url = 'https://passport.jd.com/uc/loginService'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {
    'loginName': 'neal_liu@outlook.com',
    'nloginpwd' : 'test',
    'loginpwd' : 'test',
    'uuid': '7d198199-4381-4ea5-b43b-3659d18c3fde',
    'authcode':''
    }

# headers = { 'User-Agent' : user_agent }
# data = urllib.urlencode(values)

# cookie = cookielib.CookieJar()
# cookieHandler = urllib2.HTTPCookieProcessor(cookie)

# httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler, httpsHandler, cookieHandler)
# urllib2.install_opener(opener)
# request = urllib2.Request(url, data, headers)

# try:  
#     #response = opener.open(url, data)
#     response = urllib2.urlopen(request, timeout=10)   
#     print(response.read())
# except urllib2.HTTPError, e:
#     print e.code
# except urllib2.URLError, e:
#     print e.reason
# else:
#     print "OK"


# try:  
#     my_order = opener.open('https://order.jd.com/center/list.action')
#     print my_order.read()
# except urllib2.HTTPError, e:
#     print e.code
# except urllib2.URLError, e:
#     print e.reason
# else:
#     print "OK"


resp = requests.get('http://www.bing.com')

print resp.content


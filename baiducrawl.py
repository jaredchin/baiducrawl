#coding=utf-8
import socket
import re
import urllib2

box=[]
zzz=re.compile(r"([\w\d]+\.)*[\w\d]+\.[\w\d]+")

class RedirectHandler(urllib2.HTTPRedirectHandler):  
    def http_error_301(self, req, fp, code, msg, headers):  
        print "301"  
        pass  
    def http_error_302(self, req, fp, code, msg, headers):  
        global box
        pu=headers.values()[6]
        uu=zzz.search(pu).group(0)
        if uu not in box:
            box.append(uu)
            print pu
            pass
opener=urllib2.build_opener(RedirectHandler) 


def run(content):
    zz=re.compile(r"(http://www.baidu.com/link\?url=([^\".])+)")
    
    #zloc=re.compile(r"Location:([^:.])+")
    
    #req = urllib2.Request('http://www.baidu.com/s?ie=utf-8&wd=intitle\%3Aphpmyadmin')
    #req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')
    #req.add_header('Referer', 'https://www.baidu.com/')
    #req.add_header('is_referer', 'https://www.baidu.com/')
    #r = urllib2.urlopen(req)
    #buf=r.read()
    #print buf
    u=zz.findall(content)
    for j in u:
        
        try:
            res=opener.open(j[0])
        except:
            pass




def getpage():
    for pg in range(10000):
        print "Page # [%d]" % (pg+1)
        uri="http://www.baidu.com/s?wd=intitle:phpmyadmin&pn=%d&oq=intitle:phpmyadmin&ie=utf-8&rsv_page=1" % (pg*10)
        req = urllib2.Request(uri)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')
        req.add_header('Referer', 'https://www.baidu.com/')
        req.add_header('is_referer', 'https://www.baidu.com/')
        r = urllib2.urlopen(req)    
        run(r.read())
    
getpage()

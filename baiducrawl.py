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
    u=zz.findall(content)
    for j in u:
        try:
            res=opener.open(j[0])
        except:
            pass




def getpage(data,pg_num):
    for pg in range(pg_num):
        print "Page # [%d]" % (pg+1)
        uri="http://www.baidu.com/s?wd=%s&pn=%d&oq=%s&ie=utf-8&rsv_page=1" % (data,(pg*10),data)
        req = urllib2.Request(uri)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')
        req.add_header('Referer', 'https://www.baidu.com/')
        req.add_header('is_referer', 'https://www.baidu.com/')
        r = urllib2.urlopen(req)    
        run(r.read())
    
if __name__=='__main__':
    get_search=raw_input("What Search:")
    pg_num=raw_input("Page Num[Default 10]:")
    try:
        pg_num=int(pg_num.strip())
    except:
        pg_num=10
    getpage(get_search,pg_num)

#!/usr/bin/python
#-*-coding:utf-8 -*-
import urllib2,cookielib,re,urllib,sys,os
import cPickle as p
class Client(object):
   def __init__(self):
             self.userinfo = {}
             home_dir = os.environ['HOME']
             config_file = home_dir + '/.wlt_config'
             if(os.path.isfile(config_file)):
                f = file(config_file, 'r')
                self.userinfo["username"] = f.readline().strip()
                self.userinfo["password"] = f.readline().strip()
                f.close()
             else:
                print "首次登录，请按提示操作"
                self.userinfo['username']=raw_input("请输入用户名:")
                self.userinfo['password']=raw_input("请输入密码:")
                f=file(config_file, 'w')
                f.writelines(self.userinfo['username'] + '\n')
                f.writelines(self.userinfo['password'])
                f.close()


             self.cj=cookielib.CookieJar()
             self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
             urllib2.install_opener(self.opener)
             self.type = sys.getfilesystemencoding()

   def login(self):
             params={'name':self.userinfo['username'],'password':self.userinfo['password'],'cmd':'login'}
             request=urllib2.Request(
                 "http://wlt.ustc.edu.cn/cgi-bin/ip",
                 urllib.urlencode(params)
                 )
             r=self.opener.open(request).read()
             print r.decode('gb2312').encode(self.type)
   def selectNet(self):
             params={'cmd':'set','type':'7','exp':'0'}
             request=urllib2.Request(
                 "http://wlt.ustc.edu.cn/cgi-bin/ip",
                 urllib.urlencode(params)
                 )
             r=self.opener.open(request).read()
             print r.decode('gb2312').encode(self.type)

a=Client()
a.login()
a.selectNet()



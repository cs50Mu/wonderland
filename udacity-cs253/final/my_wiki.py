# coding: utf-8
import os
import time
import webapp2
import jinja2
import cgi
import re
import hmac
import hashlib
import random
from string import letters
import time
from google.appengine.api import memcache
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
PASS_RE = re.compile(r'^.{3,20}$')
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASS_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

secret='iloveyou'
def hash_cookie(cookie):
    return '%s|%s' %(cookie,hmac.new(secret,cookie).hexdigest())

def valid_cookie(hashcookie):
    try:
        cookie = hashcookie.split('|')[0]
        if hashcookie == hash_cookie(cookie):
            return cookie
    except:
        return None

def make_salt():
    salt_list = [ random.choice(letters) for x in xrange(5) ]
    return ''.join(salt_list)

def hash_password(password,salt=None):
    if not salt:
        salt=make_salt()
    h = hashlib.sha256(password+salt).hexdigest()
    return '%s|%s' %(h,salt)

def valid_hashpassword(hashpass,password):
    salt=hashpass.split('|')[1]
    if hash_password(password,salt=salt)==hashpass:
        return True

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)



class User(db.Model):
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty()


class Signup(BaseHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.render('signup-form.html')

    def post(self):
        username=self.request.get("username")
        password=self.request.get("password")
        verify=self.request.get("verify")
        email=self.request.get("email")
        user_error = ''
        pass_error = ''
        verify_error = ''
        email_error = ''
        if valid_username(username):
            if User.all().filter('name =',username).get():
                user_error = 'This user already exists!'
        else:
            user_error="It's not a valid username!"
        if not valid_password(password):
            pass_error="It's not a valid password!"
        if (password != verify):
            verify_error="Password didn't match!"
        if (email):
            if not valid_email(email):
                email_error="It's not a valid email!"

        if (user_error or pass_error or verify_error or email_error):
            self.response.headers['Content-Type'] = 'text/html'
            self.render('signup-form.html',username=username,\
                    email=email,user_error=user_error,\
                    pass_error=pass_error,verify_error=verify_error,\
                email_error=email_error)
        else:
            h_username=hash_cookie(username)
            pw_hash = hash_password(password)
            u = User(name=username,pw_hash=pw_hash,email=email)
            u.put()
            self.response.headers.add_header('Set-Cookie','username=%s;Path=/' %str(h_username))
            self.redirect("/")       # redirect

class Login(BaseHandler):
    def get(self):
        self.render('login.html')
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        u = User.all().filter('name =',username).get()
        if u and valid_hashpassword(u.pw_hash,password):
            h_username = hash_cookie(username)
            self.response.headers.add_header('Set-Cookie','username=%s;Path=/' %str(h_username))
            self.redirect("/")       # redirect
        else:
            self.render('login.html')
           
class Logout(BaseHandler):
    def get(self):
        next_url = self.request.headers.get('referer','/')
        self.response.headers.add_header('Set-Cookie','username=;Path=/')
        self.redirect(next_url)



class PageDb(db.Model):     # database
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class NewPageHandler(BaseHandler):
    def get(self,title):
        if not title:
            title = 'mainpage'
        page = PageDb.all().filter('title =',title).get()
        if page:
            content = page.content.replace('<br>','\n')
        else:
            content = ''
        username = self.request.cookies.get('username')
        username = valid_cookie(username)
        if username:
            login = True
            self.render("newpage.html",content=content,login=login)
        else:
            self.redirect('/login')

    def post(self,title):
        if not title:
            title = 'mainpage'
        have_error = False
        content = self.request.get('content').replace('\n','<br>')    # in order for the content to be 
        params = dict(content=content)                # displayed properly in the browser
        if not content:
            have_error = True
            params['error'] = 'You need enter the content!'
        if have_error:
            self.render('newpage.html',**params)
        else:
            if PageDb.all().filter('title =',title).get():
                page = PageDb.all().filter('title =',title).get()
                page.content = content
                page.put()
            else:
                page = PageDb(title=title,content=content)
                page.put()
            if title == 'mainpage':
                title = ''
            time.sleep(1)  #  timeout for database to write, or will have weird problem
            self.redirect('/%s' % str(title))

class RandomPage(BaseHandler):
    def get(self,title):
        username = self.request.cookies.get('username')
        username = valid_cookie(username)
        if username:
            login = True
        else:
            login = False

        if not title:
            title = 'mainpage'
        page = PageDb.all().filter('title =',title).get()
        if page:
            if title == 'mainpage':
                title =''
            self.render('page.html',content=page.content,page_title=title,login=login)
        else:
            if title == 'mainpage':
                self.redirect('/_edit/')
            else:
                self.redirect('/_edit/%s' %str(title))


app = webapp2.WSGIApplication([('/_edit/(.*)', NewPageHandler),\
                            ('/signup', Signup),
                            ('/login',Login),
                            ('/logout',Logout),
                             ('/(.*)',RandomPage)],debug=True)


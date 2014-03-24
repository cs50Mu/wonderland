import os

import webapp2
import jinja2
import json
import cgi
import re
import hmac
import hashlib
import random
from string import letters


from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
PASS_RE = re.compile(r'^.{3,20}$')
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

signupForm="""
<!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
           %(user_error)s 
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="%(password)s">
          </td>
          <td class="error">
           %(pass_error)s 
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="%(verify)s">
          </td>
          <td class="error">
           %(verify_error)s 
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">
           %(email_error)s 
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

loginForm="""
<!DOCTYPE html>

<html>
  <head>
    <title>Login</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Login</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
           %(user_error)s 
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="%(password)s">
          </td>
          <td class="error">
           %(pass_error)s 
          </td>
        </tr>
     </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

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
    cookie = hashcookie.split('|')[0]
    if hashcookie == hash_cookie(cookie):
        return cookie

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


class User(db.Model):
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty()


class Signup(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(writeForm(signupForm))

    def post(self):
        username=self.request.get("username")
        password=self.request.get("password")
        verify=self.request.get("verify")
        email=self.request.get("email")
        if not valid_username(username):
            user_error="It's not a valid username!"
        else:
            user_error=''
        if not valid_password(password):
            pass_error="It's not a valid password!"
        else:
            pass_error=''
        if (password != verify):
            verify_error="Password didn't match!"
        else:
            verify_error=''
        if (email):
            if not valid_email(email):
                email_error="It's not a valid email!"
            else:
                email_error=''
        else:
            email_error=''

        if (user_error or pass_error or verify_error or email_error):
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write(writeForm(signupForm,username,password,verify,email,user_error,pass_error,verify_error,\
                email_error))
        elif User.all().filter('name =',username).get():
            user_error = 'This user already exists!'
            self.response.write(writeForm(signupForm,username,password,verify,email,user_error,pass_error,verify_error,\
                    email_error))
        else:
            h_username=hash_cookie(username)
            pw_hash = hash_password(password)
            u = User(name=username,pw_hash=pw_hash,email=email)
            u.put()
            self.response.headers.add_header('Set-Cookie','username=%s;Path=/' %str(h_username))
            self.redirect("/thanks")       # redirect

class Login(webapp2.RequestHandler):
    def get(self):
        self.response.write(writeForm(loginForm))
    def post(self):
        username=self.request.get('username')
        password=self.request.get('password')
        u=User.all().filter('name =',username).get()
        if u and valid_hashpassword(u.pw_hash,password):
            h_username=hash_cookie(username)
            self.response.headers.add_header('Set-Cookie','username=%s;Path=/' %str(h_username))
            self.redirect("/thanks")       # redirect
        else:
            self.response.write(writeForm(loginForm))
           
class Logout(webapp2.RequestHandler):
    def get(self):
        self.response.headers.add_header('Set-Cookie','username=;Path=/')
        self.redirect("/signup")


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        username=self.request.cookies.get('username')
        username=valid_cookie(username)
        if not username:
            self.redirect('/login')
        else:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Welcome, %s' %username)

def writeForm(form,username='',password='',verify='',email='',\
        user_error='',pass_error='',verify_error='',email_error=''):
    return form %{'username':username,'password':password,\
            'verify':verify,'email':email,'user_error':user_error,\
            'verify_error':verify_error,'email_error':email_error,'pass_error':pass_error}








def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class Blogdb(db.Model):     # database
    subject=db.StringProperty(required=True)
    content=db.TextProperty(required=True)
    created=db.DateTimeProperty(auto_now_add=True)

class MainPage(BaseHandler):
    def get(self):
        posts=db.GqlQuery("select * from Blogdb order by created desc")
        self.render('mainpage.html',posts=posts)

class MainPageJason(BaseHandler):
    def get(self):
        main_dict = {}
        main_list = []
        posts=db.GqlQuery("select * from Blogdb order by created desc")
        for post in posts:
            main_dict['subject'] = post.subject
            main_dict['content'] = post.content
            main_dict['created'] = post.created.strftime('%c')
            main_list.append(main_dict)
        mainJson = json.dumps(main_list)
        self.response.headers['Content-type']='application/json; charset=UTF-8'
        self.write(mainJson)



class PostPage(BaseHandler):
    def get(self,post_id):
#        key = db.Key.from_path('Blogdb',int(post_id))
#        post = db.get(key)
        post = Blogdb.get_by_id(int(post_id))

        if not post:
            self.error(404)
        else:
            self.render('permalink.html',post = post)

class postJson(BaseHandler):
    def get(self,post_id):
        post_dict = {}
        post_id = post_id.split('.')[0]
        post = Blogdb.get_by_id(int(post_id))
        if not post:
            self.error(404)
        else:
            post_dict['subject'] = post.subject
            post_dict['content'] = post.content
            post_dict['created'] = post.created.strftime('%c')
        postjson= json.dumps(post_dict)
        self.response.headers['Content-type']='application/json; charset=UTF-8'
        self.write(postjson)




class NewpostHandler(BaseHandler):
    def get(self):
#        self.render('newentry-form.html',subject='',error_subject='',\
#                content='',error_content='')
        self.render("newentry-form.html")

    def post(self):
        have_error= False
        subject=self.request.get('subject')
        content=self.request.get('content').replace('\n','<br>')    # in order for the content to be 
        params=dict(subject=subject,content=content)                # displayed properly in the browser
        if not subject:
            have_error=True
            params['error_subject']='You must have a subject!'
        if not content:
            have_error=True
            params['error_content']='You need enter the content!'
        if have_error:
            self.render('newentry-form.html',**params)
        else:
            blog=Blogdb(subject=subject,content=content)
            blog.put()
#            print blog.key().id()
            self.redirect('/%s' % str(blog.key().id()))

app = webapp2.WSGIApplication([('/newpost', NewpostHandler),\
                             ('/([0-9]+)',PostPage),
                             ('/.json',MainPageJason),
                             ('/([0-9]+\.json)',postJson),
                            ('/signup', Signup),
                            ('/thanks',ThanksHandler),
                            ('/login',Login),
                            ('/logout',Logout),
                             ('/',MainPage),],debug=True)


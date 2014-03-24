import os

import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

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

class PostPage(BaseHandler):
    def get(self,post_id):
#        key = db.Key.from_path('Blogdb',int(post_id))
#        post = db.get(key)
        post = Blogdb.get_by_id(int(post_id))

        if not post:
            self.error(404)
        self.render('permalink.html',post = post)

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
                             ('/',MainPage),],debug=True)


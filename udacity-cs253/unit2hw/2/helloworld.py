import webapp2
import cgi
import re

USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
PASS_RE = re.compile(r'^.{3,20}$')
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

form="""
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
def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASS_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(writeForm())

    def post(self):
        global username
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
            self.response.write(writeForm(username,password,verify,email,user_error,pass_error,verify_error,\
                email_error))
        else:
            self.redirect("/thanks")       # redirect


class TestHandler(webapp2.RequestHandler):
    def post(self):
        q = self.request.get("q")
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)
#        self.response.write(q)

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Welcome, %s' %username)

def writeForm(username='',password='',verify='',email='',\
        user_error='',pass_error='',verify_error='',email_error=''):
    return form %{'username':username,'password':password,\
            'verify':verify,'email':email,'user_error':user_error,\
            'verify_error':verify_error,'email_error':email_error,'pass_error':pass_error}


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform',TestHandler),
    ('/thanks',ThanksHandler),
], debug=True)


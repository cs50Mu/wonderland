import webapp2
import cgi

form="""
<form method="post">
        What is your birthday?
        <br>

        <label>Month
        <input type="text" name="month">
        </label>
        <label>Day
        <input type="text" name="day">
        </label>
        <label>Year
        <input type="text" name="year">
        </label>
        
        <br>
        <br>
	<input type="submit">
</form>
"""

textarea="""
<!DOCTYPE html>

<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""


class MainPage(webapp2.RequestHandler):

    def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)

    def post(self):
        self.response.write("Thanks! That's a totally valid day!")


class TestHandler(webapp2.RequestHandler):
    def post(self):
        q = self.request.get("q")
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)
#        self.response.write(q)

def rotate(s=''):
    rotated=[]
    if (s==''):
        return None
    else:
        for i in s:
            if i.isalpha():
                if i.isupper():
                    i=chr(((ord(i)+13-ord('A')))%26+ord('A'))
                else:
                    i=chr(((ord(i)+13-ord('a')))%26+ord('a'))
            rotated.append(i)
    return cgi.escape(''.join(rotated),quote=True)

def writeTextarea(s=''):
    return textarea %s

class Rot13Handler(webapp2.RequestHandler):
    def get(self):
        self.response.write(writeTextarea())
    def post(self):
        text = self.request.get("text")
        self.response.write(writeTextarea(rotate(text)))


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform',TestHandler),
    ('/rot13',Rot13Handler),
], debug=True)


import webapp2
import jinja2 
import os 
import logging 
from google.appengine.api import users
from google.appengine.ext import ndb 

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.dirname(__file__)))

class Posts(ndb.Model):
    name = ndb.StringProperty()
    country = ndb.StringProperty()
    post = ndb.StringProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('a_different_world.html')
        self.response.write(template.render())

class SignInHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))

class DaijonHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('aboutd.html')
        self.response.write(template.render())

class BolaHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('aboutb.html')
        self.response.write(template.render())

class NoahHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('aboutn.html')
        self.response.write(template.render())

class MapHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('map.html')
        self.response.write(template.render())

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('contact.html')
        self.response.write(template.render())

class UploadHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('upload.html')
        self.response.write(template.render())
    def post(self):
        name = self.request.get('name')
        country = self.request.get('place')
        post = self.request.get('textbox')

        post_model = Posts(
            name= name,
            country= country,
            post= post)
        post_key = post_model.put()

        post_query = Posts.query()
        list_of_posts = post_query.fetch()
        template = jinja_environment.get_template('posts.html')
        self.response.write(template.render(
            {
                'posts': list_of_posts
            }))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signin', SignInHandler),
    ('/aboutd', DaijonHandler),
    ('/aboutb', BolaHandler),
    ('/aboutn', NoahHandler),
    ('/learn', MapHandler),
    ('/contact', ContactHandler),
    ('/upload', UploadHandler),
    ('/contact', ContactHandler),
], debug=True)

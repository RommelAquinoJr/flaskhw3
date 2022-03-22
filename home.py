from flask import Flask
from flask import escape

myapp_obj = Flask(__name__)

@myapp_obj.route("/")

def home():
  name = {'name': 'Lisa'}
  return '''
  <html>
    <body>
      <h1>Welcome ''' + name['name'] + '''!</h1>
      <a href="www.google.com">not google</a>
    </body>
  </html>'''

myapp_obj.run()

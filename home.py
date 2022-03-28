from flask import Flask
from flask import escape

myapp_obj = Flask(__name__)

@myapp_obj.route("/")

#name = 'Lisa'
#city_names = ['Paris','London','Rome','Tahiti']

def home():
  #name = {'name':'Lisa'}
  city_names = ['Paris','London','Rome','Tahiti']
  return '''
  <html>
    <body>
      #<h1>Welcome ''' + name['name'] + '''!</h1>
      <h1>Welcome ''' + name + '''!</h1>
      <a href="http://www.google.com/">not google</a>
      <ul>
        <li>'''+city_names[0]+'''</li>
        <li>'''+city_names[1]+'''</li>
        <li>'''+city_names[2]+'''</li>
        <li>'''+city_names[3]+'''</li>
      </ul>
    </body>
  </html>'''

name = "Lisa"
city_names = ['Paris','London','Rome','Tahiti']
#myapp_obj.run()

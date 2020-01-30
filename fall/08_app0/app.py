# Jun Tao Lei
# SoftDev1 pd9
# K#08 -- Serving Flask routes / Flask / Serving Flask routes that directs to static webpages.
# 2019-09-18

from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='static/')

@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/about')
def about():
  return app.send_static_file('about.html')

@app.route('/contact')
def contact():
  return app.send_static_file('contact.html')

if __name__ == '__main__':
  app.debug = True
  app.run() 
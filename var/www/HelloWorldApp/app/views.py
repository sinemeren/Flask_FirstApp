from . import app
from flask import render_template

#decorator
@app.route('/')
def hello():
    return "Hello Sinem!"

@app.route('/template')
def template():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
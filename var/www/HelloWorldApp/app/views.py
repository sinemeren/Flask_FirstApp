from app import app

#decorator
@app.route('/')

def home():
    return "hello world!"
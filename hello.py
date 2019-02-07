from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello There!! This is my Flask Application.this is puppet master'
if __name__=='__main__':
    app.run()

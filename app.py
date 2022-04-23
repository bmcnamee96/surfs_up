# import dependencies
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'
@app.route('/<name>')
def my_name(name):
    return f'Hello {name}. I hope you are having a good day'




# if __name__ == '__main__':
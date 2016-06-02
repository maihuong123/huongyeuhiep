from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Huong'

@app.route('/movie')  # link html đến web. Cần import thêm render_template
def get_movie():
    return render_template('demo.html')


# @app.route('/c4e')
# def hello_c4e():
#     return 'Hello C4E'
# # để hiện Hello C4E truy cập http://127.0.0.1:5000/c4e
#
# @app.route('/c4e/1')
# def hello_team():
#     return 'Hello team 3!!!'
# # để hiện  truy cập http://127.0.0.1:5000/c4e/1
#
# @app.route('/<name>')
# def hello(name):
#     return ('Hello ' + name)
# # truy cập http://127.0.0.1:5000/, sau '/' thêm name tùy ý. Ứng dụng khi muốn truy cập đến từng bài post




if __name__ == '__main__':
    app.run()

# Day16.py: backend
# static: chứa css
# templates: chứa html

# Bước 2: tạo file html trong template
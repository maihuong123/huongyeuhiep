from flask import Flask,render_template
app = Flask(__name__)
# tại sao lại không được
class Movie:
    def __init__(self, title, img):
        self.title = title
        self.img = img

movie1 = Movie('The girl next door',)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/demo')
def demo():
    return render_template("movie.html")

if __name__ == '__main__':
    app.run()

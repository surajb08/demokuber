from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
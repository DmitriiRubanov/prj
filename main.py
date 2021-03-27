from flask import render_template, Flask, redirect

app = Flask(__name__)


@app.route('/')
def classic():
    return render_template('base.html', title='Заголовок')


@app.route('/index/<title>')
def index(title):
    if title:
        return render_template('base.html', title=title)
    else:
        return redirect('/index')


@app.route('/index')
def ix():
    return render_template('base.html', title='Заголовок')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

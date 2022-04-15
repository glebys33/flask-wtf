from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['prof'] = prof
    param['url1'] = url_for('static', filename='img/1.jpg')
    param['url2'] = url_for('static', filename='img/2.jpg')
    return render_template('specialty.html', **param)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')

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


@app.route('/list_prof/<list>')
def list_prof(list):
    param = {}
    param['list'] = list
    param['list_prof'] = [
        'инженер-исследователь',
        'пилот',
        'строитель',
        'экзобиолтог',
        'врач',
        'инженер по терроформингу',
        'климатолог',
        'специалист по радиоактивной защите',
        'астронолог',
        'гляциолог',
        'инженер жизнеобеспеченности',
        'метеоролог',
        'оператор марсохода',
        'киберинженер',
        'штурман',
        'пилот дронов',
    ]
    return render_template('professions.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

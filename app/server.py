from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def smiley():
    return 'Laba po ansible (─‿‿─)', 200, {'Content-Type': 'text/plain; charset=utf-8'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)

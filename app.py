from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args.get('a', default=0, type=float)
    b = request.args.get('b', default=0, type=float)
    return jsonify({'result': a + b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

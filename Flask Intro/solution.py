from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def index():
        return 'Hello World'

app.run(host='0.0.0.0', port=81)


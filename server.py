from flask import Flask, render_template, request
from activity import get_data
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    data_value = get_data()
    return render_template('index.html', message=data_value)
    
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
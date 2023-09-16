from flask import Flask, request, render_template_string
from medications import medications

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template_string(open('index.html').read())

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    dict_medications = medications('medications.txt')
    for key in dict_medications:
        if dict_medications[key][0] == user_input:
            return key
    return f'ID of the medication: {key}'

if __name__ == '__main__':
    app.run(debug=True)
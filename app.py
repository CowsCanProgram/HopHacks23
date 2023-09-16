from flask import Flask, request
from diagnostics_codes import diagnostics_codes

app = Flask(__name__)

@app.route('/process_input', methods=['POST'])
def process_input():
    answer = request.form['answer']
    further_info = request.form['furtherInfo']
    dictionary_diagnostics = diagnostics_codes('diagnostic_codes.txt')
    for key in dictionary_diagnostics:
        if further_info == dictionary_diagnostics[key]:
            diagnostic_key = key
    if answer == 'yes':
        print('User answered: Yes')
    elif answer == 'no':
        print(f'User answered: No, further info: {further_info} is {diagnostic_key}')

    # Add code to use the answer and further_info in your Python logic

    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'raj'

@app.route('/')
def home():
    return render_template('form.html')
@app.route('/form', methods=['POST'])
def survey_form():
    session['name']= request.form['name'], session['location'] = request.form['location'], session['fav_language'] = request.form['fav_language'], session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result_form():
    return render_template('display.html')

if __name__ == '__main__':
    app.run(debug=True)
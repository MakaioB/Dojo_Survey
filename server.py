from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'raj'

@app.route('/', methods = ['GET', 'POST'])
def survey_form():
    if request.method == 'POST':
        session['name']= request.form['name']
        session['location'] = request.form['location']
        session['fav_language'] = request.form['fav_language']
        session['comments'] = request.form['comments']
        return redirect('/result')
    else:
        return render_template('form.html')

@app.route('/result')
def result_form():
    return render_template('display.html')

if __name__ == '__main__':
    app.run(debug=True)
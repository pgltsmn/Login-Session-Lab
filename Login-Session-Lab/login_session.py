from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ufdsvzfghjk'

@app.route('/', methods = ['GET', 'POST']) # What methods are needed?
def home():
	try:
		if request.method == 'POST':
			name = request.form['name']
			login_session[name] = True
			quote = request.form['quote']
			login_session[quote] = True
			age = request.form['age']
			login_session[age] = True
			return redirect (url_for('thanks'))

		else:
			return render_template('home.html')
	except:
		return redirect (url_for('error'))


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', name = request.form[name]) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)
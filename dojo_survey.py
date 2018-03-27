from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'ftjkkt676765ju'

@app.route('/')
def create_user():
	return render_template('index.html')

@app.route('/proccess', methods=['POST'])
def see_result():


	if (len(request.form['name']) < 1 and len(request.form['comment']) < 1):
		flash("Name cannot be empty!")
		flash("Please leave a comment")
		print 'empty'
		return redirect('/')

	if len(request.form['name']) < 1:
		flash("Name cannot be empty!")
		return redirect('/')

	if len(request.form['comment']) < 1:
		flash("Please leave a comment")
		return redirect('/')

	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']

	if len(request.form['comment']) > 120:
		flash("No longer than 120 characters")
		return redirect('/')
	else:
		flash("Thanks for your comment")

	return render_template('result.html', name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])

app.run(debug=True)
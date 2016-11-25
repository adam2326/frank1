from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>', methods=['GET'])
def user_page(username):
	# next line is binding. logged in user must match the page they are requesting
	if username == users.get_current_user():
		return render_template("user_page.html", user_to_display = username)
	else:
		return "<html><body>You are not authorized to view this page.</body></html>"


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', pic=pic), 404
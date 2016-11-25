# Python modules
from flask import Flask, render_template
import jinja2
import logging

# Google modules
from google.appengine.api import users

app = Flask(__name__)




@app.route('/user/<username>', methods=['GET','POST'])
def user_page(username):
	# require user to login
	user = user.get_current_user()
	# If user is logged in
	if user:
		login_logout_url = users.create_logout_url('/')
		# next line is binding. logged in user must match the page they are requesting
		if username == user.nickname():
			# allow them to view the page
			return render_template("user_page.html", nickname = user.nickname(), login_logout_url = login_logout_url)
		else:
			# forbid viewing a page that isnt theirs
			return "<html><body>You are not authorized to view this page.</body></html>"
	else:
		login_logout_url = users.create_login_url('/')
		return "<html><body>Welcome Unkown User.  Please <a href={}>log in</a> so we know who you are.</body></html>".format(login_logout_url)



#################################################################################
#
# ERROR Handling
#
#################################################################################

@app.errorhandler(404)
def not_found_error(error):
    return 'An internal error occurred.', 404

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

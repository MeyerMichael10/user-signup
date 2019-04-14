from flask import Flask, request, redirect, render_template
import os
import cgi




app = Flask(__name__)
app.config['debug'] = True

@app.route("/")
def index():
    return render_template('sign-up.html')

@app.route("/sign_in", methods=["POST"])
def sign_in():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
#TODO: validate inputs
    if len(username) < 3 or len(username) > 20:
        username = ''
        username_error = 'Username must be between 3 and 20 characters long'
    else:
        if " " in username:
            username = ''
            username_error = 'Username cannot contain spaces'
    

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome')
    else return render_template('sign-in.html', username_error = username_error,
    password_error = password_error, verify_error = verify_error, email_error = email_error,
    username = username, password = password, verify_password = verify_password, email = email)
#TODO: add welcome page



app.run()
    
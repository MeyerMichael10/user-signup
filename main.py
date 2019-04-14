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
    if len(username) == 0:
        username = ''
        username_error = 'Username cannot be blank'
    
    if len(username) < 3 or len(username) > 20:
        username = ''
        username_error = 'Username must be between 3 and 20 characters long'
    else:
        if " " in username:
            username = ''
            username_error = 'Username cannot contain spaces'
    
    if len(password) == 0:
        password = ''
        password_error = 'Password cannot be blank'
    
    if len(password) < 3 or len(password) > 20:
        password = ''
        password_error = 'Password must be between 3 and 20 characters long'
    else:
        if " " in password:
            password = ''
            password_error = 'Password cannot contain spaces' 

    if verify_password != password:
        password = ''
        verify_password = ''
        verify_error = 'Password confirmation must match password'   

    if len(email) > 0:
        if len(email) < 3 or len(email) > 20:
            email = ''
            email_error = 'Email must be between 3 and 20 characters'
        else:
            if email.count('@') != 1 or email.count('.') != 1:
                email = ''
                email_error = 'Please enter a valid email address'
            else:
                if " " in email:
                    email = ''
                    email_error = 'Email cannot contain spaces'
            

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome')
    else:
        return render_template('sign-up.html', username_error = username_error,
        password_error = password_error, verify_error = verify_error, email_error = email_error,
        username = username, password = password, verify_password = verify_password, email = email)
#TODO: add welcome page
@app.route('/welcome')
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username = username)



app.run()
    
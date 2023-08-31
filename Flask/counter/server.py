# Importing necessary modules from the Flask framework.
from flask import Flask, render_template, session, redirect, request

# Creating an instance of the Flask class. The "__name__" argument denotes the application's module or package.
app = Flask(__name__)

# Setting the secret key for the app which is essential for Flask session functionality. This key should ideally be kept a secret.
app.secret_key = 'supercalifragilisexpealidocious'

# Defining a route for the root URL ("/"). When the root URL is accessed, the index function is called.
@app.route('/')
def index():
    # If 'counter' doesn't exist in session, initialize it to 1.
    if not 'counter' in session:
        session['counter'] = 1
    # If 'counter' already exists in session, increment it by 1.
    else:
        session['counter'] += 1

    # Render the 'index.html' template (this file should be located in a 'templates' folder).
    return render_template('index.html')

# Defining a route for "/destroy_session". When this URL is accessed, the destroy_session function is called.
@app.route('/destroy_session')
def destroy_session():
    # Clears all data from the session.
    session.clear()
    
    # Redirects the user to the root URL.
    return redirect('/')

# If this script is being run directly (and not being imported elsewhere), start the Flask app.
if __name__ == "__main__":
    # Starts the Flask application with debug mode turned on. In debug mode, the app will automatically reload upon changes.
    app.run(debug=True)


# Import necessary modules and classes
# from the Flask library.
# Flask: This is the core Flask class that
# allows you to create a new web application instance.
# render_template: This function lets you render
# an HTML template and fill it with data.
# redirect: A function to facilitate server-side redirection.
# request: This is an object that contains all
# the data sent by the client. It includes form data, headers, etc.
from flask import Flask, render_template, redirect, request

# Import the User class from the 'users' module.
# #The exact functionality of the User class isn't clear
# #from this snippet alone, but it's likely to represent users in some way,
# # perhaps providing database functionality or encapsulating user-related behavior.
from users import User

# The "__name__" variable is a built-in Python variable that evaluatesdir
# to the name of the current module. In this case, it will be '__main__' for
# the main module, but if this code is imported as a module somewhere
# else, "__name__" will be set to that module's name. By passing
# "__name__" to Flask, it knows where to look for templates, static files, etc.
app = Flask(__name__)

# This is a route decorator in Flask, which determines what URL should trigger the associated function.
@app.route('/')
# This function gets executed when the root URL ("/") of the application is accessed.
def index():
    # The `User.get_all()` function fetches all the user records, possibly from a database.
    # The exact functionality depends on the implementation of the User class, which isn't provided in the snippet.
    users = User.get_all()

    # `render_template` is a function provided by Flask to render an HTML template.
    # Here, the 'dashboard.html' template is rendered and passed the 'users' data for display.
    return render_template('dashboard.html', users=users)

# Another route decorator. This specifies that the `load_create()` function below should be triggered when "/create/new" URL is accessed.
@app.route('/create/new')
# This function is executed for the "/create/new" route.
def load_create():
    # This function simply renders the 'new.html' template, which might be a form or page to create a new user.
    return render_template('new.html')

# Another route decorator, with an added parameter: `methods=['POST']`.
# This means the associated function (below) will be triggered only when a POST request is made to the "/create/user" URL.
@app.route('/create/user', methods=['POST'])
def create():
    # This line likely saves a new user to the database using the data from the submitted form.
    # `request.form` contains the data sent with the POST request.
    User.save(request.form)

    # After saving the user, this function redirects the user to the root URL of the application.
    return redirect('/')

# This line checks if the current script is the main program and not being imported as a module elsewhere.
if __name__=="__main__":
    # If the script is the main program, it starts the Flask application with debugging enabled.
    # Debug mode will provide detailed error messages in the browser if there are any issues.
    app.run(debug=True)

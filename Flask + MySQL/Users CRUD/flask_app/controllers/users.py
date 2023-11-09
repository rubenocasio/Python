from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

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

# This is a Flask route decorator. It's a way of telling Flask that when someone accesses the "/update/{some_integer}" URL, it should run the `load_update` function. 
# The `<int:id>` portion means that the URL expects an integer value, and Flask will pass this value to the `load_update` function as the argument `id`.
@app.route('/update/<int:id>')

# This function, `load_update`, is called whenever someone accesses the "/update/{some_integer}" URL. 
# The integer in the URL will be passed into this function as the `id` argument.
def load_update(id):

    # Here, we're calling a method `get_by_id` from the `User` class. This method likely fetches a user from a database using the given `id`. 
    # Once fetched, the user data is stored in the `user` variable.
    user = User.get_by_id(id)

    # The next two lines are a basic error handling mechanism.
    # We check if the `user` variable is `None` or some falsy value (indicating that no user was found with the given `id`).
    if not user:

        # If the user wasn't found, we return a string "User not found" along with a 404 HTTP status code, which is the standard response code for "Not Found".
        return "User not found", 404

    # If a user was found, then the code proceeds to this line.
    # We're using Flask's `render_template` function to render an HTML page (`edit.html` in this case).
    # We pass the `user` data to the template, which means the template can access and display this data.
    # For instance, inside `edit.html`, you might have code that displays the user's name or email based on this data.
    return render_template('edit.html', user=user)


@app.route('/update/user/<int:id>', methods=['POST'])
def update(id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_form(data)
    return redirect('/')

@app.route('/show/<int:id>')
def show_user(id):
    user = User.get_by_id(id)
    if not user:
        return "User not found", 404
    return render_template('show.html', user=user)

@app.route('/delete/<int:user_id>')
def delete(user_id):
    User.delete(user_id)
    return redirect('/')
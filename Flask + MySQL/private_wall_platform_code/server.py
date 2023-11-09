from flask_app import app

from flask_app.controllers import users

# This line checks if the current script is the main program and not being imported as a module elsewhere.
if __name__ == "__main__":
    # If the script is the main program, it starts the Flask application with debugging enabled.
    # Debug mode will provide detailed error messages in the browser if there are any issues.
    app.run(debug = True)
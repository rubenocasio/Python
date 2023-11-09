## Import flask_app and controllers here
from flask_app import app
from flask_app.controllers import surveys

#Define our __name__ to __main__
if __name__ == "__main__":
    app.run(debug = True)

from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# @app.route('/say/flask')
# def sayFlask():
#     return 'Hi Flask!'

# @app.route('/say/michael')
# def sayMichael():
#     return 'Hi Michael!'

# @app.route('/say/john')
# def sayJohn():
#     return 'Hi John!'

# @app.route('/say/john')
# def sayJohn():
#     return 'Hi John!'

#This is because I didn't read the instructions right the first time.
@app.route('/say/<name>')
def sayName(name):
    return f'Hi {name}!'

# @app.route('/repeat/<num>/<whateva>')
# def repeat(num, whateva):
#     return f'Hi {whateva}' * int(num)

# @app.route('/repeat/<int:num>/<whateva>')
# def repeat(num, whateva):
#     return ''.join([f'Hi {whateva}' for _ in range(num)])

@app.route('/repeat/<int:num>/<whateva>')
def repeat(num, whateva):
    output = ''
    for _ in range(num):
        output += f'Hi {whateva}\n'
    return output

# Sensei Bonus
# https://flask.palletsprojects.com/en/2.2.x/errorhandling/
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
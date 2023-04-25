from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!

@app.route('/play')
def indexPlay():
    return render_template('index.html', x = 3)

@app.route('/play/<num>')
def indexPlayNum(num):
    return render_template('index.html', x = int(num), background = 'lightblue')

@app.route('/play/<num>/<color>')
def indexPlayNumColor(num, color):
    return render_template('index.html', x = int(num), background = color)


if __name__=="__main__":
    app.run(debug=True)
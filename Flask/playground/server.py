from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html", phrase="hello")

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
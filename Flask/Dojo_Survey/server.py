from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def initial():
    return render_template("index.html")

# @app.route('/results', methods=['POST'])
# def result():
#     return render_template("results.html", name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])

@app.route('/results', methods=['POST'])
def result():
    #  Use the ** syntax to unpack the form dictionary directly into the render_template function
    return render_template("results.html", **request.form)

if __name__ == "__main__":
    app.run(debug=True)
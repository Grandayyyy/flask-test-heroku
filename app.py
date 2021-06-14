from flask import Flask, render_template, request
import os

basedir=os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/test")
def test():
    blog = True
    return render_template('no-sidebar.html', blog=blog)

#products

@app.route("/advertising")
def adv():
    blog = True
    return render_template('products/advertising.html', blog=blog)

@app.route("/agriculture")
def agr():
    blog = True
    return render_template('products/agriculture.html', blog=blog)

@app.route("/mobility")
def mob():
    blog = True
    return render_template('products/mobility.html', blog=blog)

@app.route("/navigation")
def nav():
    blog = True
    return render_template('products/navigation.html', blog=blog)

@app.route("/society")
def soc():
    blog = True
    return render_template('products/society.html', blog=blog)

#trainings

@app.route("/iot")
def iot():
    blog = True
    return render_template('trainings/IOT.html', blog=blog)

@app.route("/ML")
def ml():
    blog = True
    return render_template('trainings/ML.html', blog=blog)

@app.route("/RC")
def rc():
    blog = True
    return render_template('trainings/RC.html', blog=blog)

@app.route("/robotics")
def rob():
    blog = True
    return render_template('trainings/robotics.html', blog=blog)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port='5000',debug=True, use_reloader=True)
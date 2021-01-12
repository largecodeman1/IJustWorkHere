import projects #projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, url_for, request, redirect
#create a Flask instance
app = Flask(__name__)

@app.route('/base/')
def base_route():
    return render_template("about.html", projects=projects.setup())

@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(port='5000', host='127.0.0.1')
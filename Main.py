from flask import Flask, render_template, url_for, request, redirect
#create a Flask instance
from Templates import projects

app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(port='3000', host='0.0.0.0')
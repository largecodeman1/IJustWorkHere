from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import projects #projects definitions are placed in different file
from API_test import APIQuery, test_transfer_data1, clear_data
import json

#import API_test, transfer_data1, APIQuery
# # https://flask.palletsprojects.com/en/1.1.x/api/

app = Flask(__name__)
app.config['SECRET_KEY']= 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(15), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id): 
	return User.query.get(int(user_id))

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
	email = StringField('Email', validators=[InputRequired(),Email(message='Invalid email'), Length(max=50)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm() 

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password, form.password.data):
				login_user(user, remember=form.remember.data)
				return redirect(url_for('base_route'))

		return '<h1> Invalid username or password </h1>'
		
	

	return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = RegisterForm()

	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(new_user)
		db.session.commit()
		return redirect(url_for('initial'))

	return render_template('signup.html', form=form)

@app.route('/base/')
@login_required
def base_route():
	return render_template("base.html", projects=projects.setup())

@app.route('/')
def initial():
	return render_template("initial.html", projects=projects.setup())

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('signup'))

@app.route('/riot_api_result')
@login_required
def riot_api_result():
 	return 'Hi'

@app.route('/riot_api_query', methods=["GET", "POST"])
@login_required
def riot_api_query():
	apiCallStatus = ''
	riotApiResult = ''
	name = ''
	Summoner_Id_data = clear_data()
	# POST redirection to content page
	if name != "":
		print(name)
		Summoner_Id_data = test_transfer_data1(name)
	#Summoner_Id_data = transfer_data1(name)
	#Summoner_Id_data = clear_data()
	#if request.method == 'POST':
	#	form = request.form
	#	selection = form['summoner_name']
	#	if selection == 'psy6':
	#riotApiData = GetRiotApiData(summoner_name)
	# Summoner_Id_data = transfer_data1(1)
	# apiCallStatus = 'This was the result from the server:'
	# riotApiData = 'This worked!'
	# riotApiResult = apiCallStatus + riotApiData
	#		return render_template("riot_api_query.html", Summoner_Id_data = Summoner_Id_data)
	#	#return redirect(url_for('riot_api_result', riotApiResult=riotApiResult))
	return render_template("riot_api_query.html", Summoner_Id_data = Summoner_Id_data, name=name)

@app.route('/riot_api_query/<name>', methods=["GET", "POST"])
@login_required
def riot_api_query_with_name(name):
	apiCallStatus = ''
	riotApiResult = ''
	Summoner_Id_data = clear_data()
	# POST redirection to content page
	if name != "":
		#print(name)
		#Summoner_Id_data = test_transfer_data1(name)
		Summoner_Id_data = APIQuery(name)
		#print(Summoner_Id_data)
	r = json.dumps(Summoner_Id_data)
	loaded_r = json.loads(r)
	#print(r)

	#Summoner_Id_data = transfer_data1(name)
	#Summoner_Id_data = clear_data()
	#if request.method == 'POST':
	#	form = request.form
	#	selection = form['summoner_name']
	#	if selection == 'psy6':
		#riotApiData = GetRiotApiData(summoner_name)
			# Summoner_Id_data = transfer_data1(1)
			# apiCallStatus = 'This was the result from the server:'
			# riotApiData = 'This worked!'
			# riotApiResult = apiCallStatus + riotApiData
	#		return render_template("riot_api_query.html", Summoner_Id_data = Summoner_Id_data)
	#	#return redirect(url_for('riot_api_result', riotApiResult=riotApiResult))
	return render_template("riot_api_query.html", Summoner_Id_data = loaded_r, name=name)

@app.route('/Easter Egg/')
def base_route():
	return render_template("Egg Easter.html", projects=projects.setup())

if __name__ == "__main__":
	#runs the application on the repl development server
	app.run(port='5000', host='127.0.0.1', debug = True)
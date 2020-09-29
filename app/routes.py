from flask import  render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Rishabh Manu'}
	posts = [
		{
			'author': {'username': 'Rahul'},
			'body': "It's time to Africa"
		},
		{
			'author': {'username': 'Nandu'},
			'body': "Let's Fly high!"
		}
	]
	return render_template('index.html', title="Home", user=user, posts=posts)

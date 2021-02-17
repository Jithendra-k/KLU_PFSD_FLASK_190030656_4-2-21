from flask import Flask

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return "<h1>Welcome to KL Giftshop</h1><br><a href=/login><button>login</button></a><br><a href=/register><button>Register</button></a>"

@app.route("/register")
def register():
	return "<h1>Registration successful</h1>"

@app.route("/login")
def login():
	return "<h1>Login successful</h1><br><a href=/view><button>view</button></a>"

@app.route("/view")
def view():
	return "<h1>Hi I am Jithendra.</h1>"

@app.route("/contactus")
def contactus():
	return "<h2>Contact me: 9999999999 and Email:jithendrakatta999@gmail.com</h2>"

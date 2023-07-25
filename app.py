# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Lakshya" 
    age = "16"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Prabhu Dayal" 
    age = "42"

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Meenakshi" 
    age = "39"

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def friend():

    name = "Darpan" 
    age = "15"

    return render_template('friend.html' , name = name , age = age)

# add other routes, if you want

# run the file
app.run(debug=True)

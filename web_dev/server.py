from flask import Flask, render_template

# Set the name of the Flask server script 
# as the environ variable FLASK_APP

# Use the command "flask run" to run the flask app

# Set up the server on debugg mode so we don't restart it always
# Do so by seting up the environ variable FLASK_DEBUG=True

# You may also use the clarg --debug because it's shorter
    
# Make an instance of a Flask App
app = Flask(__name__)

# Make an HTTP route for the main page

# Allow dynamic naming for routes with <>
@app.route("/")
def say_hi():
    return "I said Hi"

@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template("./index.html", name=username, post_id=post_id)


# Make an HTTP route for the about page
@app.route("/about.html")
def blog_thoughts():
    return render_template("./about.html")

@app.route("/blog")
def blog():
    return "<h1>My Blog</h1>"

@app.route("/blog/2020/dogs")
def blog2():
    return "2020 Dogs"

# Make a blog route

# Run the Flask App
#if __name__ == "__main__":
    #app.run()

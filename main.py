from flask import Flask, render_template

project = Flask(__name__)

@project.route("/")
def render():
  return render_template('mainpage.html')

project.run(host="0.0.0.0", debug=True)
from beltexam import app
from beltexam.controllers.controller import Controller
from flask import render_template
controller=Controller()
@app.route("/", methods=["GET"])
def opener(): 
    return render_template("index.html")
@app.route('/register', methods=['POST'])
def register():
    return controller.register()
@app.route('/login', methods=['POST'])
def login():
    return controller.login()
@app.route('/loggedin', methods=['GET','POST'])
def loggedin():
    return controller.loggedin()
@app.route('/logout', methods=['GET','POST'])
def logout():
    return controller.logout()
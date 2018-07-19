from flask import Flask, render_template, request, redirect, flash, session
from beltexam.models.model import Model
model=Model()
class Controller:
    def register(self):
        response=model.register(request.form)
        if response[0] == []:
            session['name']= response[1]
            return redirect('/loggedin')
        else:
            for i in response[0]:
                flash(i)
            return redirect("/")
    def login(self):
        response = model.login(request.form)
        if response[0] == []:
            session['name']=response[1]
            return redirect("/loggedin")
        else:
            for i in response[0]:
                flash(i)
            return redirect("/")
    def loggedin(self):
        if 'name' not in session:
            flash("You must log in first!")
            return redirect('/')
        else:
            return render_template("loggedin.html",name=session['name'])
    def logout(self):
        session.clear()
        return redirect('/')
import re
from beltexam.config.mysqlconnection import connectToMySQL
from beltexam import app
from flask_bcrypt import Bcrypt
app.secret_key = "theMostSecret"
mysql = connectToMySQL('mydb')
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Model:
    def register(self, form):
        flasharr = []
        responsearr=[]
        if len(form["f_name"]) < 1:
            flash.append["Name can't be blank!"]
        if form['f_name'].isalpha() == False:
            flash.append["Name must be alpha!"]
        if len(form["l_name"]) < 1:
            flash.append["Last Name can't be blank!"]
        if form['l_name'].isalpha() == False:
            flash.append["Last Name can't be alpha!"]
        if len(form['email'])< 1:
            flash.append["Email cant be blank"]
        if not EMAIL_REGEX.match(form['email']):
            flash.append['Invalid Email Format']
        if len(form["pw"]) < 8:
            flash.append["Password must be 8 characters!"]
        if form["pw"] != form['pwc']:
            flash.append["Passwords must match!"]
        query = "SELECT * FROM users where email = %(email)s;"
        data = {'email': form['email']}
        all_users = mysql.query_db(query, data)
        if len(all_users) > 0:
            flash.append["Email already registered!"]
        if flasharr!=[]:
            responsearr.append(flasharr)
            return responsearr
        elif flasharr==[]:
            username= form['f_name']+" "+form['l_name']
            query = "INSERT INTO users (f_name,l_name,email,password) VALUES (%(f_name)s,%(l_name)s,%(email)s,%(password)s);"
            data = {
                    'f_name': form['f_name'],
                    'l_name': form['l_name'],
                    'email': form['email'],
                    'password': bcrypt.generate_password_hash(form['pw'])
                }
            newuserid = mysql.query_db(query, data)
            responsearr.append(flasharr)
            responsearr.append(username)
            return responsearr
    def login(self,form):
        flasharr=[]
        responsearr=[]

        if len(form['liemail'])< 1:
            flasharr.append("email cannot be blank!")
        if not EMAIL_REGEX.match(form['liemail']):
            flasharr.append("email not valid")
        if len(form["lipw"]) < 8:
            flasharr.append("password minimum length is 8 characters")
        if flasharr != []:
            responsearr.append(flasharr)
            return responsearr
        elif flasharr== []:
            query = "SELECT * FROM users WHERE email = %(email)s;"
            data = {
                    'email': form['liemail']
                }
            usercheck = mysql.query_db(query,data)
            if bcrypt.check_password_hash(usercheck[0]['password'], form['lipw'])==True:
                username = usercheck[0]['f_name']+" "+usercheck[0]['l_name']
                responsearr.append(flasharr)
                responsearr.append(username)
                return responsearr
            else:
                flasharr.append("you could not be logged in")
                responsearr.append(flasharr)
                return responsearr
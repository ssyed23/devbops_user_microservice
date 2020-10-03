from flask import Flask, render_template, request, url_for, redirect
from user_functions import Users
user = Users()
app = Flask(__name__)






@app.route('/register', methods=['POST'])
def signup():
   
    res = request.json
    username = res["Username"]
    password = res["Password"]
    email = res["Email"]

    firstname = res["FirstName"]
    lastname = res["LastName"]
    currentcity = res["City"]
    currentcountry = res["Country"]

    if user.verifying_email_and_user_are_available( username, currentcity, currentcountry, email, firstname, lastname, password):
        
        return {
        "Result":  True
    }
    else:
        return {
        "Result": False
    }





@app.route("/login",  methods=['POST'])
def login():
    
    res = request.json
    username = res["Username"]
    password = res["Password"]
    res = user.authincate_user(username, password)
    # True / False
    return {
        "Result": res
    }
    


    

# @app.route("/after_login")
# def after_login(usr):
#     print(usr)
#     return f"hey {usr} thanks for registering !!"

    
 


if __name__ == "__main__":
    app.run(debug=True)


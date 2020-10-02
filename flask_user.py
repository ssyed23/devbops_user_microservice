from flask import Flask, render_template, request, url_for, redirect
from user_functions import users

test = users()
app = Flask(__name__)




@app.route("/")
def home():
    return redirect(url_for("signup"))

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        user = request.form["Username"]
        test.put(user)
        return redirect(url_for("user", usr=user))

    
    else:
        return render_template("signup.html")



@app.route("/<usr>")
def user(usr):
    print(usr)
    return f"hey {usr}"
    
 


if __name__ == "__main__":
    app.run(debug=True)


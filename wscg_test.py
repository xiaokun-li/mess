# _*_ coding:utf-8 _*_

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__, template_folder="xxx")
app.secret_key = "djfakaljkaadfaljlk1k2lji234laldf"

user_list = {
    "1": {"name": "terry", "age": 45},
    "2": {"name": "iori", "age": 42},
    "3": {"name": "kyo", "age": 46},

}


@app.route("/index")
def index():
    user_info = session.get("user_info")

    if user_info:
        return render_template("index.html", user_list=user_list)
    else:
        return redirect("/login")


@app.route("/detail")
def detail():
    user_info = session.get("user_info")
    if not user_info:
        return redirect("/login")

    uid = request.args.get("uid")
    user_detail = user_list.get(uid)
    return render_template("detail.html", user_detail=user_detail)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "hpdemo" and password == "test1234":
            session["user_info"] = username
            return redirect("/index")
        else:
            return render_template("login.html", errormsg="username or password is error~")
    return render_template("login.html")


@app.route("/logout")
def logout():
    del session["user_info"]
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True, port=8899, host="0.0.0.0")

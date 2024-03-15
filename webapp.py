from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

account = {
}

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/create-account")
def render_createAccount():
    return render_template('createAccount.html')

@app.route("/account")
def render_account():
    if "username" in account:
        new_user_password = request.args["new_password"]

        account["password"] = new_user_password

        return render_template('account.html', new_password = new_user_password, new_name = account["username"])

    else:
        user_name = request.args['user_name']
        user_password= request.args['user_password']

        account["username"] = user_name
        account["password"] = user_password
        
        return render_template('account.html', new_name = user_name, new_password = user_password)

@app.route("/new-password")
def render_newPassword():
    current_password = account["password"]

    return render_template('newPassword.html', old_password = current_password)
    
if __name__=="__main__":
    app.run(debug=True)
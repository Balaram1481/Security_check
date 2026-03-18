from flask import Flask, request

app = Flask(__name__)

# Hardcoded credentials (security issue)
USERNAME = "admin"
PASSWORD = "admin123"

@app.route("/")
def home():
    return "Welcome to DevSecOps Demo App"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Insecure authentication (no hashing)
        if username == USERNAME and password == PASSWORD:
            return "Login Successful"
        else:
            return "Invalid Credentials"

    return '''
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit">
        </form>
    '''

# Debug mode ON (security issue)
if __name__ == "__main__":
    app.run(debug=True)
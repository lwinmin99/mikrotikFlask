from flask import Flask, render_template, url_for, flash, redirect, request
import requests
from form import RegistrationForm, LoginForm

url = "https://192.168.113.111/rest/ip/address"
header = {
    "Authorization": 'Basic bHdpbm1pbmtvOmx3aW5taW5rbzEyMw==',
}
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/", methods=["DELETE", "GET"])
def home():
    response = requests.get(url, headers=header, verify=False)
    datas = response.json()
    return render_template('home.html' , datas=datas)

@app.route("/about", methods=["POST", "GET"])
def about():
    if request.method == "POST":
        address = request.form["address"]
        interface = request.form["interface"]
        payload = { "address" : address, "interface": interface}
        response = requests.put(url, headers=header, json = payload , verify=False)
        datas = response.json()
        return render_template('detail.html', datas=datas)
    else:
        return render_template("about.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
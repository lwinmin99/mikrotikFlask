from flask import Flask, render_template, url_for, flash, redirect
import requests
from form import RegistrationForm, LoginForm

header = {
    "Authorization": 'Basic bHdpbm1pbmtvOmx3aW5taW5rbzEyMw==',
}
response = requests.get("https://192.168.113.111/rest/ip/address", headers=header, verify=False)

datas= response.json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
def home():
    return render_template('home.html', datas=datas)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():   
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)
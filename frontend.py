from flask import Flask, render_template, redirect, request, url_for
from forms import SignUpForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '54bed9a3aef0167858e71664dd1ba697'

@app.route('/')
def home():
    return signup()
#    return 'Hello Underworld'
#def home():   

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result = result)

    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
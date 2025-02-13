from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def profile():
    return render_template('index.html')

@app.route('/profile')
def redirect_profile():
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)

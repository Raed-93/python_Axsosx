
from flask import Flask, render_template, request,redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1  
    return render_template('index.html', count=session['counter'])

@app.route('/increment', methods=['POST'])
def increment():
    increment = int(request.form['increment_value'])
    session['counter'] += increment - 1
    return redirect('/')

@app.route('/incrementBy2', methods=['POST'])
def incrementBy2():
    session['counter'] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/') 


if __name__ == "__main__":
    app.run(debug=True)
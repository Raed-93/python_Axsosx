from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
        print(f"New number generated: {session['number']}")
    else:
        print(f"Existing number in session: {session['number']}")
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['attempts'] += 1
    guess = int(request.form['guess'])

    if guess < session['number']:
        session['result'] = 'Too low!'
        session['color'] = 'red'
    elif guess > session['number']:
        session['result'] = 'Too high!'
        session['color'] = 'red'
    else:
        session['result'] = f'Correct! The number was {session["number"]}. You guessed it in {session["attempts"]} attempts.'
        session['color'] = 'green'

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

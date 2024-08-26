from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

leaderboard = []

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['result'] = None
        session['guesses'] = 0
        print(f"New number generated: {session['number']}")
    else:
        print(f"Existing number in session: {session['number']}")
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['attempts'] += 1
    guess = int(request.form['guess'])
    
    if session['attempts'] >= 5 and guess != session['number']:
        session['result'] = f"You Lose! The number was {session['number']}. Try again!"
        session['color'] = 'red'
        return redirect('/')

    if guess < session['number']:
        session['result'] = 'Too low!'
        session['color'] = 'blue'
    elif guess > session['number']:
        session['result'] = 'Too high!'
        session['color'] = 'red'
    else:
        session['result'] = f'Correct! The number was {session["number"]}. You guessed it in {session["attempts"]} attempts.'
        session['color'] = 'green'
        return redirect('/winner')

    return redirect('/')

@app.route('/winner', methods=['GET', 'POST'])
def winner():
    if request.method == 'POST':
        name = request.form['name']
        leaderboard.append({'name': name, 'attempts': session['attempts']})
        session.clear()
        return redirect('/leaderboard')
    return render_template('winner.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/leaderboard')
def leaderboard_page():
    return render_template('leaderboard.html', leaderboard=leaderboard)

if __name__ == "__main__":
    app.run(debug=True)

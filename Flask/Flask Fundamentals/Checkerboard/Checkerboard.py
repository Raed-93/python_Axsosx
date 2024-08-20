from flask import Flask, render_template

app = Flask(__name__)


@app.route('/play/<int:x>/<int:y>/<color1>/<color2>')
def play_x(x,y,color1,color2):
    return render_template('index.html', number1 = x, number2 = y, box_color1 = color1, box_color2 = color2)



if __name__ == "__main__":
    app.run(debug=True)
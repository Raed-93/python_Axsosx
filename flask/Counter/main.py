from flask import Flask, render_template
app = Flask(__name__)

counter = 0
@app.route('/')
def counter():
    global counter
    counter += 1
    return render_template("index.html", count = counter)

if __name__ == '__main__':
    app.run(debug=True)
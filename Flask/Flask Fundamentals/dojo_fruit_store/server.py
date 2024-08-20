from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    straw = request.form['strawberry']
    ras = request.form['raspberry']
    app = request.form['apple']
    name = request.form['first_name']
    lastName = request.form['last_name']
    studentId = request.form['student_id']
    
    return render_template("checkout.html", straw_on_form=straw, ras_on_forme=ras, app_on_form=app, name_on_form=name, last_on_form=lastName, studentId_on_form=studentId)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
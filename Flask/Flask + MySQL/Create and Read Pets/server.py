from flask import Flask, render_template,redirect,request
from mysqlconnection import connectToMySQL  # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('pet')	# call the function, passing in the name of our db
    pets = mysql.query_db('SELECT * FROM pets;')  # call the query_db function, pass in the query as a string
    print(pets)
    return render_template("index.html",all_pets=pets)

@app.route("/create_pet", methods=["POST"])
def add_friend_to_db():
    print(request.form)
    
    query = "INSERT INTO pets (name, type, created_at, updated_at)VALUES (%(n)s, %(tp)s, NOW(), NOW());"
    
    data = {
        "n": request.form["pname"],
        "tp": request.form["ptype"],
    }
    
    mysql = connectToMySQL("pet")
    mysql.query_db(query, data)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template,redirect,request
from mysqlconnection import connectToMySQL  # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('first_flask')	# call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html",all_friends = friends)

@app.route('/friend/<int:id>')
def show_friend(id):
    query = "SELECT * FROM friends WHERE id = %(id_num)s;"
    
    data = {'id_num': id}
    
    mysql = connectToMySQL("first_flask")
    friend = mysql.query_db(query, data)
    
    return render_template("friend.html", friend=friend)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    print(request.form)
    
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)VALUES (%(fn)s, %(ln)s, %(occup)s, NOW(), NOW());"
    
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "occup": request.form["occ"]
    }
    
    mysql = connectToMySQL("first_flask")
    mysql.query_db(query, data)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


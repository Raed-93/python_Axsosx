from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'  # يجب إعداد مفتاح سري لاستخدام الجلسات

# مسار لعرض جميع المستخدمين
@app.route('/users')
def index():
    mysql = connectToMySQL('user')
    users = mysql.query_db('SELECT * FROM users;')
    return render_template('all_users.html', all_users=users)

# مسار لانشاء مستخدم جديد
@app.route('/create_user', methods=['POST'])
def create_user():
    print(request.form)
    
    # استرجاع البيانات من النموذج
    first_name = request.form['fname']
    last_name = request.form['lname']
    email = request.form['email']
    
    # التحقق من أن جميع الحقول غير فارغة
    if not first_name or not last_name or not email:
        flash('All fields are required!')
        return redirect('/')

    mysql = connectToMySQL("user")
    
    # الاستعلام مع اسم الجدول الصحيح
    query = """
        INSERT INTO users (first_name, last_name, email, created_at, updated_at) 
        VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());
    """
    
    data = {
        "fname": first_name,
        "lname": last_name,
        "email": email,
    }
    
    try:
        mysql.query_db(query, data)
        flash('User added successfully!')
    except Exception as e:
        print(f"Database error: {e}")
        flash(f"An error occurred: {e}")

    return redirect('/users')

# مسار اخر لنفس الرابط لعرض ملف new_user.html
# يجب ان يكون هناك مسارين واحد للعرض ويكون من نوع GET 
#واخر لانشاء مستخدم جديد من نوع POST
@app.route('/create_user', methods=['GET'])
def show_create_user_form():
    return render_template('new_user.html')

@app.route('/show/user/<int:user_id>', methods=['GET'])
def show_user(user_id):
    mysql = connectToMySQL("user")
    query = "SELECT * FROM users WHERE user_id = %(id)s;" 
    # user_id هي نفسها المعرفه في الرابط وداخل قوس الداله
    # id يجب ان تكون مطابقه لما بين القوس الازرق
    data = {"id": user_id}
    user = mysql.query_db(query, data)
    
    if not user:
        flash("User not found!", "error")
        return redirect("/users")
    # user هي التي تستعمل داخل ملف shoe_user.html
    return render_template('show_user.html', user=user[0]) 

# الرابط الاول الخاص بجلب البيانات
# يجب انشاء رابطين للتعديل واحد لجلب اليبانات ويكون من نوع GIT
# والثاني يكون من نوع post لارسال البيانات
@app.route('/edit/user/<int:user_id>', methods=['GET'])
def edit_user(user_id):
    mysql = connectToMySQL('user')
    query = "SELECT * FROM users WHERE user_id = %(id)s;"
    data = {"id": user_id}
    user = mysql.query_db(query, data)
    
    if not user:
        flash("user not found!", "error")
        return redirect("/users")
    
    return render_template('edit_user.html', user=user[0])

#الرابط الثاني الخاص بارسال التعديل
@app.route('/update/user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    mysql = connectToMySQL('user')
    
    first_name = request.form['fname']
    last_name = request.form['lname']
    email = request.form['email']
    
    query = """
    UPDATE users
    SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW()
    WHERE user_id = %(id)s;
    """
    
    data = {
        "fname": first_name,
        "lname": last_name,
        "email": email,
        "id": user_id
    }
    
    mysql.query_db(query, data)
    
    return redirect("/users")


@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    mysql = connectToMySQL("user")
    
    # حذف السجل بناءً على معرفه
    query = "DELETE FROM users WHERE user_id = %(id)s;"
    data = {
        "id": user_id
    }
    mysql.query_db(query, data)
    return redirect("/users")



if __name__ == "__main__":
    app.run(debug=True)
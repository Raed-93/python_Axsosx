from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'  # يجب إعداد مفتاح سري لاستخدام الجلسات

# المسار الرئيسي لعرض جميع الحيوانات الأليفة وإضافة حيوان أليف جديد
@app.route('/')
def index():
    mysql = connectToMySQL('pet')
    pets = mysql.query_db('SELECT * FROM pets;')
    return render_template('index.html', all_pets=pets)

# المسار لإضافة حيوان أليف جديد إلى قاعدة البيانات
@app.route('/create_pet', methods=['POST'])
def create_pet():
    print(request.form)
    
    pet_name = request.form['pname']
    pet_type = request.form['ptype']
    
    # التحقق من أن الحقول ليست فارغة
    if not pet_name.strip() or not pet_type.strip():
        flash("All fields are required!", "error")
        return redirect("/")
    
    mysql = connectToMySQL("pet")
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW());"
    
    data = {
        "name": pet_name,
        "type": pet_type,
    }
    

    mysql.query_db(query, data)
    
    return redirect("/")

@app.route('/delete_pet/<int:pets_id>', methods=['POST'])
def delete_pet(pets_id):
    mysql = connectToMySQL("pet")
    
    # حذف السجل بناءً على معرفه
    query = "DELETE FROM pets WHERE pets_id = %(id)s;"
    data = {
        "id": pets_id
    }
    mysql.query_db(query, data)
    
    # التحقق مما إذا كانت قاعدة البيانات فارغة
    # AUTO_INCREMENT
    # check_empty_query = "SELECT COUNT(*) as count FROM pets;"
    # count_result = mysql.query_db(check_empty_query)
    
    # if count_result[0]['count'] == 0:
    #     # إعادة تعيين AUTO_INCREMENT إذا كانت قاعدة البيانات فارغة
    #     reset_auto_increment_query = "ALTER TABLE pets AUTO_INCREMENT = 1;"
    #     mysql.query_db(reset_auto_increment_query)
    
    return redirect("/")

@app.route('/edit_pet/<int:pets_id>', methods=['GET'])
def edit_pet(pets_id):
    mysql = connectToMySQL('pet')
    query = "SELECT * FROM pets WHERE pets_id = %(id)s;"
    data = {"id": pets_id}
    pet = mysql.query_db(query, data)
    
    if not pet:
        flash("Pet not found!", "error")
        return redirect("/")
    
    return render_template('edit_pet.html', pet=pet[0])

@app.route('/update_pet/<int:pets_id>', methods=['POST'])
def update_pet(pets_id):
    mysql = connectToMySQL('pet')
    
    pet_name = request.form['pname']
    pet_type = request.form['ptype']
    
    if not pet_name.strip() or not pet_type.strip():
        flash("All fields are required!", "error")
        return redirect(f"/edit_pet/{pets_id}")
    
    query = """
    UPDATE pets
    SET name = %(name)s, type = %(type)s, updated_at = NOW()
    WHERE pets_id = %(id)s;
    """
    
    data = {
        "name": pet_name,
        "type": pet_type,
        "id": pets_id
    }
    
    mysql.query_db(query, data)
    
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)

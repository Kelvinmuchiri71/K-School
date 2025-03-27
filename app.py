from models import Student, db
from flask import Flask, request, jsonify
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                           #tracks all modifications

db.init_app(app)
migrate = Migrate(app,db)                                                      #tracks the schema


@app.route('/hello')
def hello():
    return '<h1>Hello K Muchiri<h1>'

@app.route('/students', methods=['GET'])
def get_all_students():
    #will return a list of all students

    all_students = Student.query.all()                                      #query the database
    students_list= [std.to_dict() for std in all_students]                  #converts students list to dictionaries
    return jsonify(students_list)

#POST method

@app.route('/students', methods=['POST'])
def create_student():
    #Creates a new student

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400
    try:
        new_student = Student(name=data['name'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify(new_student.to_dict()), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    #will return a sinlgle student by ID

    student = Student.query.get(student_id)                                    #query the database
    if not student:
        return jsonify({"Error: Student not found"}), 404
    return jsonify(student.to_dict())


#PATCH method

@app.route('/students/<int:students_id>', methods=['PATCH'])
def update_student(student_id):
    #updates a students information by ID

    student = Student.query.get(student_id)                                    #query the database
    if not student:                                                            #if no student with that id, return the error
        return jsonify({"error: Student not found"}), 404
    
    data = request.get_json()                                                  #extracts data and converts its into a JSON request, returns a python dictionary (with key n value)

    if not data:                                                               #if the data extracted cannot be converted into a JSON request then return the error
        return jsonify({"Error: Invalid request"}), 400
    try:
        if 'name' in data:                                                     #if the key exits form the data extracted then change the name
            student.name = data['name']
        db.session.commit()
        return jsonify(student.to_dict())
    except KeyError:                                                           #if the key from the dictionary(extracted data) does not exits, bring forth the error and return
        return jsonify({"error: Invalid fields"}), 400
    

#DELETE request

@app.route('/students/<int:students_id>', methods=['DELETE'])
def delete_student(student_id):
    #deletes a student by ID

    student = Student.query.get(student_id)               
    if not student:                                                            
        return jsonify({"Error: Student not found"}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
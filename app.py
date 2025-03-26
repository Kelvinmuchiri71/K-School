from models import app, Student

@app.route('/hello')
def hello():
    return '<h1>Hello K Muchiri<h1>'


@app.route('/all_students')
def get_all_students():
    #will return a list of all students
    all_students = Student.query.all()
    students_list= []
    for students in all_students:
        students_list.append(students.to_dict())
    return students_list


if __name__ == '__main__':
    app.run()
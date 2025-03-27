#create 105 students


from models import app, Student, db #Teacher
from faker import Faker

fake = Faker()

with app.app_context():
    Student.query.delete()
    students = [Student(name=fake.name()) for i in range(105)]
    db.session.add_all(students)
    db.session.commit()
    print("All students added successfully")

# with app.app_context():
#     Teacher.query.delete()
#     students = [Student(name=fake.name()) for i in range(105)]
#     db.session.add_all(teachers)
#     db.session.commit()
#     print("All teachers added successfully")
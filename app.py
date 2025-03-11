from flask import Flask, jsonify

todo = Flask('__name__')
students=[{
        'id':104,
        'student_name': 'std1',
        'age':21,
        "email":'sana@gmail.com'
   },
        {'id':105,
        'student_name': 'std2',
        'age':22,
        "email":'sana@gmail.com'
   },
        {'id':106,
        'student_name': 'std3',
        'age':23,
        "email":'sana@gmail.com'
   }
]

@todo.route('/students-list')
def students_list():

    return jsonify(students)

@todo.route('/student/get/<int:id>')
def student_get_by_id(id):
    for std in students:
        if std['id']==id:
            return jsonify(std)

        print(id)
    return jsonify (id)

if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )


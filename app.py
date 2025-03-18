from flask import Flask, jsonify

todo = Flask('__name__')
students =[ {
        'id' : 1,
        'student_name' : 'std1',
        'age' : 21,
        'email': 'hello@gmail.com'
    },
    {
        'id': 2,
        'student_name': 'std2',
        'age': 22,
        'email': 'World@gmail.com'
    },
        {
            'id': 3,
            'student_name': 'std3',
            'age': 23,
            'email': 'World@gmail.com'
        },
        {
            'id': 4,
            'student_name': 'std4',
            'age': 23,
            'email': 'google@gmail.com'
        },
        {
            'id': 5,
            'student_name': 'std5',
            'age': 25,
            'email': 'World@gmail.com'
        },
        {
            'id': 6,
            'student_name': 'std6',
            'age': 23,
            'email': 'MyHelloWorld@gmail.com'
        },
        {
            'id': 7,
            'student_name': 'std7',
            'age': 23,
            'email': 'Worldsami@gmail.com'
        },
        {
            'id': 8,
            'student_name': 'std8',
            'age': 23,
            'email': 'World@gmail.com'
        },
        {
            'id': 9,
            'student_name': 'std9',
            'age': 23,
            'email': 'World@gmail.com'
        },
        {
            'id': 10,
            'student_name': 'std10',
            'age': 23,
            'email': 'World@gmail.com'
        }
]


@todo.route('/students-list')
def students_list():

    return jsonify(students)

@todo.route('/students-list/restapi')
def students_list_restapi():
    import requests

    url = "https://rest-api-dev1-awq2.onrender.com/students-list"

    payload = {}
    headers = {}

    response = requests.request("GET", url)

    return response.json()



@todo.route('/student/get/<int:id>')
def get_students_by_id(id):
  for std in students:
      if std['id'] == id:
          return jsonify(std)

      return "id not found"


if __name__ == '__main__':
    todo.run(
        debug=True
    )
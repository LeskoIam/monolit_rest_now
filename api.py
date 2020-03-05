from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with

app = Flask(__name__)
api = Api(app)

# Data
TODOS = {
    "todo1": {"task": "build an API"},
    "todo2": {"task": "?????"},
    "todo3": {"task": "profit!"},
}


parser = reqparse.RequestParser()
parser.add_argument("task")
parser.add_argument("smth")  # Test


# Represents single Todo item
# Returns single Todo item
# Delete Todo item
class Todo(Resource):

    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204  # 204: no content

    def put(self, todo_id):
        args = parser.parse_args()
        print(args)
        task = {"task": args["task"]}
        TODOS[todo_id] = task
        return task, 201  # 201: created


# Represents complete todo "list"
# Add new todos with POST
class TodoList(Resource):

    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        print(args)
        todo_id = int(max(TODOS.keys()).lstrip("todo")) + 1
        todo_id = f"todo{todo_id:d}"
        TODOS[todo_id] = {"task": args["task"]}
        return TODOS[todo_id], 201


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message=f"Todo {todo_id} doesn't exist")

# ##############################################################


# Data - represents "database response object"
class MyTodos:
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task
        self.created_on = "Today"


resource_fields = {
    "delo":   fields.String(attribute='task'),
    "todo_id": fields.String,
    "created_on": fields.String
    }


class MyTodoList(Resource):

    @marshal_with(resource_fields)
    def get(self):
        return MyTodos("todo22", "get beer")


# Api routing
api.add_resource(TodoList, "/v1/todos")
api.add_resource(Todo, "/v1/todos/<todo_id>")

api.add_resource(MyTodoList, "/v1/mytodo")

if __name__ == "__main__":
    app.run(debug=True)

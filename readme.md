1. GET tasks by id (Todo)
   - curl http://localhost:5000/v1/todos/todo3 -v

2. GET all tasks (TodoList)
   - curl http://localhost:5000/v1/todos -v

3. DELETE a task (Todo)
   - curl http://localhost:5000/v1/todos/todo2 -X DELETE -v

4. Add a new task (TodoList)
   - curl http://localhost:5000/v1/todos -d "task=something new" -X POST -v

5. Update a task (Todo)
   - curl http://localhost:5000/v1/todos/todo3 -d "task=something different" -X PUT -v
   
X. My TODO demonstrate fields
   - curl http://localhost:5000/v1/mytodo -v
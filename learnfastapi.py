from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = ["Tidy my room", "Clean the house", "Clean the house", "Cook", "Take a bath", "Go for a walk", "Shopping groceries"]

#@app.get("/")
#async def root():
#    return {"message": "Hello World"}

#@app.get("/tasks") This can also be seen as another method...
#async def getTasks():
#    task = tasks
#    return {"tasks": f"{tasks}"}

@app.get("/")
async def get_tasks():
    number_of_tasks = len(tasks)
    return {"task_information": f"You have {number_of_tasks} tasks left open.", "tasks": f"{tasks}"}


class Task(BaseModel):
    taskname: str


@app.post("/")
async def add_tasks(task: Task):
    tasks.append(task.taskname)
    return {"status": "Task got added successfully!", "added_task": f"Taskname: {task.taskname}"}

@app.delete("/")
async def delete_tasks(task: Task):
    if task.taskname in tasks: #IMPORTANT TO REMEMBER FOR FUTURE PROJECTS
        tasks.remove(task.taskname)
        return {"status": "Task got deleted successfully!", "deleted_task": f"Taskname: {task.taskname}"}
    else:
        return {"error": "404 Task not found"}






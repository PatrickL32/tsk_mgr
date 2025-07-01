from flask import Flask, request

from app.database import task

app = Flask(__name__)

@app.get("/")
@app.get("/tasks")
def get_all_tasks():
    out = {"tasks": task.scan(), "ok": True}
    return out

@app.get("/tasks/<int:pk>")
def get_single_task(pk):
    out = {"task": task.select_by_id(pk), "ok": True}
    return out

@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    return "", 204

@app.put("/tasks/<int:pk>")
def update_task(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204

@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete_by_id(pk)
    return "", 204

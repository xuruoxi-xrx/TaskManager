from storage import load_tasks,save_tasks#添加了读取和重写
def add_task(title):#我想加这个叫title的任务
    tasks=load_tasks()#先在json里读取
    new_id=max((task["id"] for task in  tasks),default=0)+1#给这个任务编号
    new_task={
        "id": new_id,
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task
def view_tasks():
    tasks=load_tasks()
    return tasks
def complete_task(task_id):
    tasks=load_tasks()
    for task in tasks:
        if task["id"]==task_id:
            task["completed"]=True
            save_tasks(tasks)
            return True
    return False
def delete_task(task_id):
    tasks=load_tasks()
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False

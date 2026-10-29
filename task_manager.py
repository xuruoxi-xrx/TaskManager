from storage import load_tasks,save_tasks
def add_task(title,priority,due_date):#我想加这个叫title的任务
    tasks=load_tasks()#先在json里读取
    new_id=max((task["id"] for task in  tasks),default=0)+1#给这个任务编号
    new_task={
        "id": new_id,
        "title": title,
        "completed": False,
        "priority":priority,
        "due_date":due_date
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
def search_tasks(keyword):
    tasks=load_tasks()
    results=[]
    for task in tasks:
        if keyword.lower() in task["title"].lower():
            results.append(task)
    return results

def filter_tasks(completed):
    tasks=load_tasks()
    result=[]
    for task in tasks:
        if completed==task["completed"]:
            result.append(task)
    return result
def task_statistics():#任务统计
    tasks=load_tasks()
    total=len(tasks)
    completed_count=0
    for task in tasks:
        if task["completed"]:
            completed_count+=1
    imcompleted_count=total-completed_count
    if total==0:
        result=0
    else:
        result=completed_count/total*100
    return total,completed_count,imcompleted_count,result


    







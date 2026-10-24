from task_manager import add_task,view_tasks,complete_task,delete_task
while True:
    print("========== 待办事项管理系统 ==========")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 完成任务")
    print("4. 删除任务")
    print("0. 退出系统")

    choice = input("请选择功能：")
    if choice=="0":
        print("感谢使用，再见！")
        break
    elif choice == "1":
        title=input("请输入任务名称：").strip()
        if not title:
            print("任务名称不能为空！")
        else:
            add_task(title)
            print("任务添加成功！")
    elif choice =="2":
        tasks = view_tasks()
        if not tasks:
            print("当前没有任何任务!")
        else:
            for task in tasks:
                if task["completed"]:
                    status="已完成"
                else:
                    status="未完成"
                print(task["id"],task["title"],status)
    elif choice=="3":
        try:
            task_id=int(input())
        except ValueError:
            print("请输入正确的数字")
        else:
            result=complete_task(task_id)
            if result:
                print("任务已完成！")
            else:
                print("任务不存在！")

    elif choice=="4":
        try:
            task_id=int(input())
        except ValueError:
            print("请输入正确的数字")
        else:
            result=delete_task(task_id)
        if result:
            print("任务删除成功！")
        else:
            print("任务不存在！")
    else:
        print("无效选项，请重新选择！")








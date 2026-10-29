from task_manager import add_task,view_tasks,complete_task,delete_task,search_tasks,filter_tasks,task_statistics
from datetime import datetime
def display_task(task):
    if task["completed"]:
        status = "已完成"
    else:
        status = "未完成"

    priority = task.get("priority","中")
    due_date = task.get("due_date","") or "无"
    print(f"[{task["id"]}] {task["title"]} | {status} | 优先级：{priority} | 截止日期: {due_date}")

while True:
    print("========== 待办事项管理系统 ==========")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 完成任务")
    print("4. 删除任务")
    print("5. 搜索任务")
    print("6. 筛选任务")
    print("7. 任务统计")
    print("0. 退出系统")

    choice = input("请选择功能：")
    if choice=="0":
        print("感谢使用，再见！")
        break
    elif choice == "1":
        title=input("请输入任务名称：").strip()
        while True:
            due_date=input("请输入截止日期：").strip()
            if due_date=="":
                break
            try:
                date=datetime.strptime(due_date,"%Y-%m-%d")
                result=date.strftime("%Y-%m-%d")
                if result!=due_date:
                    raise ValueError
                print("日期合法")
                break
            except ValueError:
                print("日期不合法")
        priority=input("请输入优先级（高/中/低）：").strip()
        while priority not in ["高","中","低"]:
            print("输入错误")
            priority=input("请重新输入：").strip()
        if not title:
            print("任务名称不能为空！")
        else:
            add_task(title,priority,due_date)
            print("任务添加成功！")
    elif choice =="2":
        tasks = view_tasks()
        if not tasks:
            print("当前没有任何任务!")
        else:
            priority_order={
                "高":3,
                "中":2,
                "低":1
            }
            sorted_tasks=sorted(
                tasks,
                key=lambda task: priority_order[task.get("priority","中")],
                reverse=True
            )
            for task in sorted_tasks:
                display_task(task)
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
    elif choice=="5":
        keyword=input("请输入搜索关键词：").strip()
        results=search_tasks(keyword)
        if not results:
            print("没有找到匹配任务")
        for result in results:
           display_task(result)
    elif choice=="6":
        option=input("1. 已完成的任务  2. 未完成的任务：").strip()
        results=[]
        if option=="1":
            results=filter_tasks(True)
        elif option=="2":
            results=filter_tasks(False)
        else:
            print("选项无效")
        if option in ["1","2"]:
            if not results:
                print("没有符合的条件")
            else:
                for result in results:
                    display_task(result)
    elif choice=="7":
        a,b,c,d=task_statistics()
        print(f"总任务数：{a} 已完成数：{b} 未完成数: {c} 完成率：{d:.1f}%")





    else:
        print("无效选项，请重新选择！")









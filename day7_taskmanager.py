import os
import json
import csv

#file to store task
File_name="task.txt"

#load task from file
def load_task():
    task={}
    if os.path.exists(File_name):
        with open(File_name,"r") as file:
            for line in file:
                task_id,title,status,deadline,priority=line.strip().split("|")
                task[int(task_id)]={"title":title,"status":status, "deadline":deadline, "priority":priority}
    return task

# save task to File 
def save_task(task):
    with open(File_name,"w") as file:
        for task_id, info in task.items():
            file.write(f"{task_id}|{info["title"]}|{info["status"]}|{info["deadline"]}|{info["priority"]}\n")
            
# Export tasks to JSON file
def export_to_json(task):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(task, f, indent=4)
    print("Tasks exported to tasks.json")

def export_to_csv(task):
    with open("tasks.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Task ID", "Title", "Status", "Deadline", "Priority"])
        for task_id, info in task.items():
            writer.writerow([task_id, info['title'], info['status'], info['deadline'], info['priority']])
    print("Tasks exported to tasks.csv")
                    
# add a new task
def add_task(task):
    title = input("Enter the title name")
    deadline = input("Enter the deadline of the task (e.g. 2025-07-10)")
    priority = input("Enter the priority of the task (high/ low / medium)")
    task_id= max(task.keys(),default=0)+1
    task[task_id]={"title":title,"status":"Incomplete","deadline":deadline,"priority":priority}
    print(f" task {title} added")
    
# veiw all tasks
def view_task(task):
    if task=={}:
        print("no task avaliable")
    else:
        for task_id , info in task.items():
            print (f"[{task_id}]| {info["title"]} - {info["status"]} - {info["deadline"]} - {info["priority"]}")
            
#mark task as complete
def mark_task_complete(task):
    task_id=int(input("please enter the task_id to mark up as complete"))
    if task_id in task:
        task[task_id]["status"]="completed"
        print(f"{task[task_id]["title"]} marked up as completed")
    else: 
        print("task_id not found")
        
#change task priority
def change_task_priority(task):
    task_id=int(input("please enter the task_id to change the priiority"))
    priority=input("Enter the priority of the task (high/ low / medium)")
    if task_id in task:
        task[task_id]["priority"]=priority
        print(f"{task[task_id]["title"]} changed priority")
    else: 
        print("task_id not found")
        
# delete task
def delete_task(task):
    task_id=int(input("please enter the task_id to delete"))
    if task_id in task:
        deleted_task=task.pop(task_id)
        print(f"{deleted_task["title"]} deleted")
    else: 
        print("task_id not found")
        
def main():
    task=load_task()
    while True:
        print("\n task manager menu")
        print("1. add task")
        print("2. view tasks")
        print("3. mark task as completed")
        print("4. delete task")
        print("5. change task priority")
        print("6. exit")
        print("7. export to JSON")
        print("8. export to CSV")
        
        choice= input("please enter your choice")
        
        if choice=="1":
            add_task(task)
        elif choice=="2":
            view_task(task)
        elif choice=="3":
            mark_task_complete(task)
        elif choice=="4":
            delete_task(task)
        elif choice=="5":
            change_task_priority(task)
        elif choice=="7":
            export_to_json(task)
        elif choice=="8":
            export_to_csv(task)
        elif choice=="6":
            save_task(task)
            print("goodby")
            break
        else:
            print("invalid choice")

if __name__=="__main__":
    main()            
    
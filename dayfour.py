
tasks=[]




while True:
  
  print("Enter 1.add task:")
  print("Enter 2.remove a task:")
  print("Enter 3.view all tasks:")
  print("Enter q to quit:")

  user_choice  =input("please enter your selection:")
  
  if user_choice== "q":
    break

  if user_choice== "1":
    title=input("Enter title:")
    priority=input("Enter priority as 'H', 'M','L':")
    task={"title":title, "priority":priority}
    tasks.append(task)
    print(task)
  
  if user_choice== "3":

    for item in tasks:
      print(item["title"])
      print(item["priority"])

  if user_choice== "2":
     
    delete_tasks=input("which item do you want to remove:")

    del tasks[(int(delete_tasks))-1]
       
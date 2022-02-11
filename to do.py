print("....###...TASK REMINDER...###....")

     

task=int(input("HOW MANY TASK YOU HAVE TO DO:"))
task3=[]
for i in range(task):
    element=input("enter the task:")
    # status=input("enter the ststus:")
    task3.append(element)
print("list elements are:")
print("....TASKS.....")
for i in range(len(task3)):
    print(task3[i])
print(task3)
edit=input("YOU WANY TO EDIT THIS TASK....SAY...yes or no...=")
if edit=="yes":
    add=input("WHAT WANT TO ADD THIS TASK=")
    task3.append(add)
else:
    print("ohk next")
print(task3) 
for i in range(len(task3)):
    print(task3[i])
done=int(input("HOW MANY TASK YOU HAD  DONE="))
i=1
c=[]
while i <=done:
    done_1=input("WHICH TASK YOU HAD DONE=")
    c.append(done_1)
    
    i=i+1
print(c)    

j=0
d=[]
while j <len(task3):
    # print(task3[j])
    if task3[j] not in c:
        d.append(task3[j])  
    j=j+1
print(d ,"are remaining tasks")  


processing=int(input("HOW MANY TASK IS IN PROCESSING"))
i=1
e=[]
while i <=processing:
    processing_1=input("WHICH TASK IS IN PROCESSING=")
    e.append(processing_1)
    i=i+1
print(e,"is in processing")

v=0
f=[]
while v <len(task3):
    if task3[v] not in e:
        f.append(task3[v])
        v=v+1
print(f,"are in processing task")


rem=input("you want to reminder on any task")
if rem=="yes":
    rem_1=input(" on which task=")
    print(rem_1,"reminder on this task")
else:
    print("ohk next")




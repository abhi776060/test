def subjects(n):
    marks_data={}
    for x in range(n):
        subject_name = input("enter subject name")
        subject_marks = int(input("enter subject marks"))
        marks_data[subject_name] = subject_marks
    return marks_data

def update():
    a=subjects()
    for key, value in a.items():
        if (value < 75):
            print("Enter marks of subject ", key, " : ")
            sub = int(input())
            a[key] = sub
n=int(input("enter subjects"))
a=subjects(n)
num=0
for x in a.values():
    num += x
percentage = num / len(a.keys())
print('{}%'.format(percentage))
if percentage > 95:
        print("gold medal and distinction", )

elif percentage > 90:
        print("distinction")
elif percentage > 75:
        print("average")
elif percentage < 75:
    count = 0
    for x in a.values():
        if x >= 75:
            count += 1
    if count >= 3:
        update()


else:
        print("failed")





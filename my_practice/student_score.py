def my_marks():
    score = {}
    name = input('enter subject name :')
    marks = float(input('enter subject marks :'))
    score[name] = marks
    num = list(score.values())
    return num


num = my_marks()
total = 0
print(num)
for x in num:
    total += x
    percentage = (total / (len(num)))
    if percentage >= 75:
            print("Percet")
    else:
        print("Failed....Enter again!!!")
        my_marks()







my_marks()






def gradingStudents(grades):
    # Write your code here
    # fives_list=[x for x in range(30,101,5)]
    list1=[]
    for x in grades:
        if x <35:
            list1.append(x)
        else:
            ele1=x//10
            ele2=ele1*10
            ele3=x-ele2
            actual_num=0
            if ele3 <5:
                actual_num=ele2+int('5')
            elif ele3>5:
                actual_num=ele2+int('10')
            diff=abs(x-actual_num)
            if diff >=3:
                list1.append(x)
            else:
                list1.append(actual_num)
    print(list1)
gradingStudents([73,67,38,33])
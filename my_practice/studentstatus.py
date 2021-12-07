class student:
    def __init__(self,sub1,sub2,sub3,sub4,sub5,sub6):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5
        self.sub6 = sub6
    def a(self):
        total_marks=[self.sub1,self.sub2,self.sub3,self.sub4,self.sub5,self.sub6]
        marks=0
        for x in total_marks:
            marks+=x
        percentage=(marks/600)*100
        total_marks.sort()
        a=total_marks[3:]
        a1,a2,a3=a
        if percentage >90 :
            print("distinction")
            if a1>=90 and a2>=90 and a3>=90:
                print('gold medal')
        elif percentage>=75 and percentage<=90:
            print("average")
        else:
            print("failed")



sub1 =int(input("enter marks sub1 :"))
sub2 = int(input("enter marks sub2:"))
sub3 = int(input("enter marks sub3:"))
sub4 = int(input("enter marks :"))
sub5 = int(input("enter marks :"))
sub6 = int(input("enter marks :"))
abhi = student(sub1, sub2, sub3, sub4, sub5, sub6)
abhi.a()
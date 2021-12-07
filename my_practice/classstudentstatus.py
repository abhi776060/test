class student:
    def __init__(self,sub1,sub2,sub3,sub4,sub5,sub6):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5
        self.sub6 = sub6

class update(student):
        def uupdate(self):
            b=a.__dict__
            for key, value in b.items():
                if (value < 75):
                    print("Enter marks of subject ", key, " : ")
                    sub = int(input())
                    b[key] = sub
a1=int(input("   sub   "))
b=int(input("   sub   "))
c=int(input("   sub   "))
d=int(input("   sub   "))
e=int(input("   sub   "))
f=int(input("   sub   "))
a=update(a1,b,c,d,e,f)
print(a.__dict__)
marks=list(a.__dict__.values())
mark=0
for x in marks:
    mark+=x
percentage=mark/6
print(percentage)
if percentage >95:
    print("distinction and gold medal")
elif percentage > 90:
    print("distinction ")
    data1 = a.__dict__
    count = 0
    for y in data1.values():
        if y <= 75:
            count += 1
    print(count)
    if count >= 3:
        a.uupdate()

        print("pass")
elif percentage >=75 and percentage<=90 :
    print("average")

else:
    print('failed')

class Student:
    def first_input(self):
        n = int(input("Enter number of subjects : "))
        total_subject=0
        sub_marks = {}
        for i in range(n):
            sub = input("Subject name : ")
            marks = int(input("Marks of"))
            sub_marks[sub] = marks
            total_subject +=1
        self.sub_marks=sub_marks
        print(self.sub_marks)



    def re_input(self):
        for key,value in self.sub_marks:
            if(value < 75):
                self.sub_marks[key] = int(input("Enter marks of ",key," again : "))

    def pass_fail(self):
        if(3 <= self.total_subject <= 7):
            failed_sub_no = calculate_no_of_failed()
            if(failed_sub_no == 0):
                grade()
            elif(failed_sub_no <= 3):
                re_input()
                grade()
            else:
                print("You have failed in ",failed_sub_no," so you are FAIL!!")

    def grade(self):
        sum = 0
        for m in self.sub_marks.values():
            sum += m
        total_per = sum/self.total_subject
        if(total_per > 95):
            print("Distinction + Gold")
        elif(total_per > 90):
            print("Distinction")
        elif(total_per > 75):
            print("Average")
        else:
            print("FAILED")

    def calculate_no_of_failed(self):
        fail_count = 0
        for key, value in self.sub_marks:
            if(value < 75):
                fail_count += 1
        return fail_count
obj=Student()
obj.first_input()
obj.pass_fail()

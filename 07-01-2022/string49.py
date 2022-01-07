#count and display the vowels of a given text
class String:
    def __init__(self):
        pass

    def count_vowels(self,str1):
        vowels_list=['a','e','i','o','u']
        str2=''
        count=0
        for x in str1:
            if x in vowels_list:
                count+=1
        print(count)

solution=String()
solution.count_vowels("abhishek")
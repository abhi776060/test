#that accepts a string and calculate the number of digits and letters
class String:
    def __init__(self):
        pass

    def calc(self,str1):
        letters=0
        number=0
        for x in str1:
            if x.isdigit():
                number+=1
            else:
                letters+=1

        print(f"letters: {letters}   numbers: {number}")

string1=String()
string1.calc("W3resource")
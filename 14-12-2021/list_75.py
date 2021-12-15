#Write a Python program to convert month name to a number of days

class List:
    def __init__(self):
        pass

    def check(self,str1):
        month_name=str1.lower()
        if month_name == "february":
            print("No. of days: 28/29 days")
        elif month_name in ("april", "june", "september", "november"):
            print("No. of days: 30 days")
        elif month_name in ("january", "jarch", "may", "july", "august", "october", "december"):
            print("No. of days: 31 day")
        else:
            print("Wrong month name")
me=List()
month_name = input("Input the name of Month: ")
print(me.check(month_name))

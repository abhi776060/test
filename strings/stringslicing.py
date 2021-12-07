class Slicing():
    def make_substring(self,chars, start=0, stop=0, step=0):
        s = ""
        for i in range(start, stop, step):
            if i >= len(chars):
                break 
            s += chars[i]
        return s

me=Slicing()
print(me.make_substring('abhishek',0,8,1))
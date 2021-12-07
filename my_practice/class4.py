class Language:
    def say_hello(self):
        raise NotImplemented("please use say_hello class in your child class")
class French(Language):
    pass
    #def say_hello(self):
     #   return "bronue"
class Chinese(Language):
    def say_hello(self):
        return "chugo"
def into(language):
    return language.say_hello()

abhi=French()
vishnu=Chinese()
into(abhi)

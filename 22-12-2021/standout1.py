class Number:
    def divide(self,num1, num2):
        sign = -1 if ((num1 < 0) ^ (num2 < 0)) else 1  # if both inputs are same then it is falls either of the input is ture or false return true

        num1 = abs(num1)
        num2 = abs(num2)
        '''
        10/2=5      13/3=4.333~~4
        
        '''
        quotient = 0
        while num1 >= num2:
            num1 =num1- num2
            quotient =quotient+ 1

        if sign == -1:
            quotient = -quotient

        print(quotient)

div=Number()
div.divide(10,-2)



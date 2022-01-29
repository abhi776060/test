def birthdayCakeCandles(candles):
    # Write your code here
    new_list=sorted(candles)
    end=new_list[-1]
    cou=new_list.count(end)
    print(cou)
birthdayCakeCandles([3,2,1,3])
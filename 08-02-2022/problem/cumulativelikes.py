
from ctypes import c_ulong


def viralAdvertising(n):
    # Write your code here
    cumulative=0
    share=5
    for x in range(n):
        # print(share,cumulative)
        liked=share//2
        cumulative+=liked
        share=liked*3

    return cumulative
   
print(viralAdvertising(5))
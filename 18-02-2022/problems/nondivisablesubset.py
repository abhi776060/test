from collections import defaultdict
def nonDivisibleSubset(k, s):
    # Write your code here
    mods = [item % k for item in s]
    freqs = defaultdict(int)

    for elem in mods:
        freqs[elem] += 1
    total = 0
    print(freqs.items())
    print(mods)
    for key, val in freqs.items():
        if val == 0:
            continue
        if key == 0:
            total += 1
        elif (k - key) == key:
            total += 1
        elif key > (k - key): 
            if (k - key) in freqs:
                total +=  max([val, freqs[k - key]])
            else:
                total += val
        elif key < (k - key):
            if (k - key not in freqs):
                total += val
    return(total)
print(nonDivisibleSubset(4,[19,10,12,10,24,25,22]))
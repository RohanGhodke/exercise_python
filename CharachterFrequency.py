s1 = "codekul.com"

frequency = {}

for i in s1:
    if i in frequency:
        frequency[i] += 1
    
    else:
        frequency[i] = 1

print("Count of all charachters in the string is:",frequency)                     
    
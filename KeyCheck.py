d1 = {1 : 'Red' , 2 : 'Blue' , 3 : 'Green'}

k = int(input("Enter key to check if already exists:"))

for i in d1:
    if i == k:
        print('Key already exists')
        break
    else:
        print('Key does not exists') 
        break   
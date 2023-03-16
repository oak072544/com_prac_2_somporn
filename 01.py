t = int(input("Enter temperature : "))
if t > 30 :
    print('Hot')
elif 20 < t <= 30 :
    print('Warm') 
elif 10 < t <= 20 :
    print('Fine')
elif t <= 10 :
    print('Cold')
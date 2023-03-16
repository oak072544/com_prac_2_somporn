k = eval(input("Enter number : "))
count = 0
for j in range( 1, k+1 ) :
   
   if j%7 == 0 :
        count += 1
        
print("Count = ",count)
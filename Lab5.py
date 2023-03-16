model = ["iPhone 12","Samsung Galaxy Note20","Sony Xperoa 1 II","HTC U11 Plus"]
Branch = ["สาขา A","สาขา B","สาขา C","สาขา D"]
x = [[120,240,300,500],[80,200,200,100],[350,100,400,380],[200,300,380,50]]
print("iPhone 12 number 0\nSamsung Galaxy Note20 number 1\nSony Xperoa 1 II number 2\nHTC U11 Plus number 3")
m = int(input("รุ่นสมาร์ทโฟน : "))
print("สาขาใดขายสมาร์โฟนรุ่น",model[m],"ได้สูงสุด")
y = m
z = x[y][0]
for i in range(0,4):
    if x[y][i] > z:
        b = i
        c = 2
        z = x[y][i]
if x[y][1]==x[y][2]:
    print(Branch[b],"และ",Branch[c],"ขายสมาร์ทโฟนรุ่น",model[m],"ได้สูงสุด")
else:
    print(Branch[b],"ขายสมาร์ทโฟนรุ่น",model[m],"ได้สูงสุด")
#print(Branch[b],"ขายสมาร์ทโฟนรุ่น",model[m],"ได้สูงสุด")
list1=[]
list2=[]

n=int(input("enter the no of ele in L1: "))
for i in range(n):
    l=input("enter values")
    list1.append(l)
m=int(input("enter the no of ele in L2: "))
for i in range(m):
    l=input("enter values")
    list2.append(l)

print("intersection of two list", set(list1) & set(list2))
print("union of two lists: ", set(list1)|set(list2))



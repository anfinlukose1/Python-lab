#to add the elements of an array/list
print("Enter the size :")
size=int(input())
a=[int(i)for i in range(size)]
sum=0
print("Entar elements \n");
for i in range(size):
    a[i]=int(input())
    sum+=a[i]
    print("\nThe sum of the elements in the  array is::%d"%(sum))

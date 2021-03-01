def maxminposition(A,n):
    minposition=A.index(min(A))
    maxposition=A.index(max(A))
    print("the maximum is at position:-",maxposition+1)
    print("maximum element: -",max(A))
    print("the minimum is at position:-",minposition+1)
    print("minimum element: -",min(A))
A=list()
n=int(input("Enter the size of the list:-"))
print("Enter the element:-")
for i in range(int(n)):
    k=int(input(""))
    A.append(k)
maxminposition(A,n)

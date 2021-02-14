m=int(input("Enter maths number:"))
e=int(input("Enter english number:"))
c=int(input("Enter chemistry number:"))
p=int(input("Enter physics number:"))
ph=int(input("Enter physical education number:"))
t=m+e+c+p+ph/5
print("total is"+str(t))
if p<50:
  print("Grade C")
elif p<80:
  print("Grade B")
else:
  print("Grade A")

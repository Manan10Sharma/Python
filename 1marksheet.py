maths=int(input("Enter maths number:-"))
english=int(input("Enter english number:-"))
chemistry=int(input("Enter chemistry number:-"))
physics=int(input("Enter physics number:-"))
physical_education=int(input("Enter physical_education number:-"))
total=maths+english+chemistry++physics+physical_education
print("total marks=",total)
percentage=total/5
print("percentage=",percentage,"%")
if percentage>90:
  print("Grade A")
elif percentage>70:
  print("Grade B")
elif percentage>50:
  print("Grade C")
elif percentage>36:
  print("Grade d")
else:
  print("fail")
    

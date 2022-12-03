print(("-"*40).rjust(79, ' '))
print(("Pratice1").rjust(63, ' '))
print(("-"*40).rjust(79, ' '))

No = input("No = ")
Name = input("Name = ")
Grade = float(input("Grade = "))
Class = input("Class = ")

out_text = "My no. is {} and my name is {}. I have grade {} and in class {}".format(
    No, Name, Grade, Class)
print("-"*(len(out_text)+10))
print(' '*5, out_text, ' '*5, sep='')
print("-"*(len(out_text)+10))

A = int(input("A= "))
B = int(input("B= "))
C = int(input("C= "))

print("-"*70)

print("A+B-C = ", int(A+B-C))
print("A-(B+C) = ", int(A-(B+C)))
print("A/C*B = ", int((A/C*B)))
print("-"*70)
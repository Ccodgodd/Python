#2)
n=int(input("Enter the number of days the user is sitting:"))
if n<=5:
  print(n)
  print(n*2,"Rs")

elif 6<=n<=10:
  print(n)
  print(n*3,"Rs")
elif 11<=n<=15:
  print(n)
  print(n*4,"Rs")
else:
  print(n)
  print(n*5,"Rs")
#3)
n=int(input("Enter the number:-"))
if n%2==0:
  if 2<=n<=5:
    print("NOT WIERD")
  elif n>20:
    print("NOT WIERD")
  else:
    print(" ")
else:
  print("WIERD")
  #1)
  ch=str(input("enter the alphabet :"))
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print("it is a vowel")
else:
    print("it is not a vowel")

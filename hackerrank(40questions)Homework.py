# Question: Write a loop that prints numbers from a variable `j` as long as it is in another variable `i`.
###################################################################################################
while j in i:
    print(j)
    j = j + 1

# Question: Calculate the wind chill index based on air temperature and wind velocity.
n = int(input("Enter the air temp: \n"))
m = int(input("Enter the velocity: \n"))
WCM = 35.74 + 0.6215 * n - 35.75 * m**0.16 + 0.4275 * n * m**0.16
print(WCM)
###################################################################################################

# Question: Print the lyrics of a poem with proper formatting.
t = '''Twinkle, twinkle, little star,
 How I wonder what you are! Up above the world so high,
 Like a diamond in the sky. Twinkle, twinkle, little star,
  How I wonder what you are'''
print(t)
###################################################################################################

# Question: Print the current version of Python and the current date and time.
import sys
t = sys.version
print(t)

import datetime
r = datetime.datetime.now()
print(r)
###################################################################################################

# Question: Create a list of numbers from 0 to a user-defined number and convert it to a tuple.
r = int(input("Enter the total numbers you need to write:\n"))
i = 0
li = []

for i in range(i, r + 1):
    li.append(i)

print(li)
r = tuple(li)
print(r)
###################################################################################################

# Question: Calculate the sum of all natural numbers up to a given number.
import datetime
r = datetime.datetime.now()
print(r)

n = int(input("Enter the natural number till you want to find the sum:"))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print(sum)
###################################################################################################

# Question: Print the current user and convert Celsius to Fahrenheit.
import getpass
r = getpass.getuser()
print(r)

n = float(input("Enter the Celsius you want to convert: "))
f = (n * (9 / 5) + 32)
print(f)
###################################################################################################

# Question: Calculate the factorial of a given number.
n = int(input("Enter the number for which you want to find the factorial: "))

if n == 0 or n == 1:
    print(1)
else:
    fact = 1
    for i in range(n, 1, -1):
        fact = fact * i
    print("\nThe factorial of {} is {}".format(n, fact))
###################################################################################################

# Question: Print the multiplication table of a given number.
n = int(input("Enter the multiplication table you want to see: "))
for i in range(1, 21):
    print(n, "x", i, "=", n * i)
###################################################################################################

# Question: Count from 1 to a given number.
n = int(input("Enter the number till where you want to count..."))
for i in range(1, n + 1):
    print(i, end=" ")
###################################################################################################

# Question: Calculate the sum of all even numbers up to a given number.
n = int(input("Enter the number till where you want to find the addition of even numbers: "))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum = sum + i
        print(i)
print("The total sum of the even numbers is:=", sum)
###################################################################################################

# Question: Reverse a string and print each character.
r = "Nandhu"
for i in r[8:0:-1]:
    print(i)

k = int(input("Enter the factorial you want to find...."))
n = 1
for i in range(1, k + 1):
    n = n * i
    print(n)
###################################################################################################

# Question: Check if numbers in a list are prime.
print("Prime number checker....")

li = [1, 3, 4, 5, 6, 7, 8, 9]
for n in li:
    if n <= 1:
        print("It's not a prime number....")
    elif n % 4 == 0:
        print("It's not a prime number...")
    elif n % 5 == 0 and n != 5:
        print("It's not a prime number....")
    elif n % 6 == 0:
        print("It's not a prime number....")
    elif n % 7 == 0 and n != 7:
        print("It's not a prime number....")
    elif n % 8 == 0:
        print("It's not a prime number....")
    elif n % 9 == 0:
        print("It's not a prime number....")
    else:
        print("It's a prime number")
###################################################################################################

# Question: Identify repeated elements in a list.
t = set()
type(t)
li = [1, 2, 3, 5, 5, 667, 55, 55, 66, 667, 45]
for i in li:
    if i in t:
        print(i)
    else:
        print(i, "is repeated again and again")
###################################################################################################

# Question: Print numbers in decreasing and increasing order.
n = int(input("Enter the number till where you need to iterate: "))
for i in range(n, 0, -1):
    print(i, end=" ")
    print("\n")
for j in range(1, n + 1):
    print(j, end=" ")
###################################################################################################

# Question: Print elements in a list of fruits.
li = ["Orange", "Apple", "Grape", "Strawberry"]
for i in li:
    print(i)
###################################################################################################

# Question: Print key-value pairs in a dictionary.
dic = {
    'country': 'capital',
    'india': 'delhi',
    'kerala': 'trivandrum',
    'tn': 'chennai',
}
for i in dic:
    print(i, dic[i])
###################################################################################################

# Question: Check and print whether numbers are odd or even.
n = int(input("Enter the number till you want to check odd/even: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
    else:
        print("Hey!...it's odd", i)
print("Total number of elements is", i)
###################################################################################################

# Question: Calculate the total sum of even numbers.
n = int(input("Enter the number to find the total sum of even numbers: "))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum = sum + i
    else:
        continue
print("The total sum of the even number is:=", sum)
###################################################################################################

# Question: Check for prime numbers within a range.
n = int(input("Enter the number till you want to see the prime numbers: "))

for i in range(1, n + 1):
    if n <= 1:
        print("Not allowed")
        continue
    elif i == 2:
        print(i, end=" ")
        continue
    elif i % 2 == 0 or i == 1:
        continue
    elif i % 3 == 0 and i != 3:
        continue
    elif i % 4 == 0:
        continue
    elif i % 5 == 0 and i != 5:
        continue
    elif i % 6 == 0:
        continue
    elif i % 7 == 0 and i != 7:
        continue
    elif i % 8 == 0:
        continue
    elif i % 9 == 0:
        continue
    else:
        print(i, end=" ")
        continue
###################################################################################################

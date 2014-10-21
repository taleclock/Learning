from sys import argv

script, cap, m, n = argv 

# Count multiples up to cap 
cap = int(cap)
# First multiple
m = int(m)
# Second multiple
n = int(n)

sum = 0

for i in range(0,cap):
  if i % m == 0:
    print(i)
    sum += i
  elif i % n == 0:
    print(i)
    sum += i
  else:
    print ("-")

print ("\nSum:")
print (sum)
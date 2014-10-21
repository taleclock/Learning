from sys import argv

script, num = argv 

n = int(num)
sum = 0

for i in range(0,n):
  if i % 3 == 0:
    print(i)
    sum += i
  elif i % 5 == 0:
    print(i)
    sum += i
  else:
    print ("-")

print ("\nSum:")
print (sum)
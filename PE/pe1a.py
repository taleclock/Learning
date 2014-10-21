from sys import argv

script, cap, m, n = argv 

# Count multiples up to cap 
cap = int(cap)
# First multiple
m = int(m)
# Second multiple
n = int(n)

# Sum of the multiples of m, n, and m*n
multSumM = 0
multSumN = 0
multSumMN = 0

# Create a list of multiples of m up to cap
for i in range(m,cap,m):
  print(i)
  multSumM += i

# Create a list of multiples of n up to cap
for i in range(n,cap,n):
  print(i)
  multSumN += i

# Create a list of multiples of m and n up to cap  
for i in range((m*n),cap,(m*n)):
  print(i)
  multSumMN += i

# Add the sums of the multiples of m and n
# Subtract multiples of both m and n, to erase any duplicates
sum = multSumM + multSumN - multSumMN

# Print the sum of the multiples of m and n
print ("\nSum:")
print (sum)
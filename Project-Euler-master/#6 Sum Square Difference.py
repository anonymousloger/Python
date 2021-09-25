sumOfSquare = 0       # sum of squares of number
squreOFSum = 0       # square of sum of numbers
sum = 0
start = 1
end = 100
for i in range(start, end+1):
    sumOfSquare += (i*i)
    sum += i
squreOFSum = sum * sum
print ("Result=",abs(sumOfSquare - squreOFSum))

# completed
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

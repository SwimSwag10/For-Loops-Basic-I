for val in range(151):
  print(val)

for val in range(5,1000,5):
  print(val)

for val in range(1,100):
  if val % 10 == 0:
    print("Coding Dojo")
  elif val % 5 == 0:
    print("Coding")

sum=0
for val in range(1,500000,2):
  sum = sum+val
print(sum)

count = 2018
while count > 0:
  if count % 2 == 0:
    print(count)
  count-=4

# Flexible Counter - Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3
for val in range(lowNum, highNum+1):
  if val % mult == 0:
    print(val)
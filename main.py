from random import*
def oneTrial ():
  roll1 = randint(0,5)==5
  roll2 = randint(0,5)==5
  roll3 = randint(0,5)==5
  roll4 = randint(0,5)==5
  numRolls =4
  tee = 0
  if(roll1 ==True or roll2 == True or roll3 == True or roll4 == True):
    tee = tee+1
  return tee

sum = 0
count = 0
while count<1000:
  sum = sum+oneTrial()
  count +=1
print( sum/count)
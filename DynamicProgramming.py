__author__ = 'dongpei'
import time



def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

print(recMC([1,5,10,25],63))


def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

# Dong: The reason R is way much slower is because R passes the value of known
# Result initiately instead of caching knownResult
def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for c in coinValueList:
           if(change >= c):
               numCoins = 1 + recDC(coinValueList, change-c, knownResults)
               if numCoins < minCoins:
                   minCoins = numCoins
                   knownResults[change] = minCoins
   return minCoins

start_time = time.clock()
recDC([1,5,10,25],63,[0]*64)
print (time.clock() - start_time, "seconds")


coinValueList = [1,5,10,25]

def dpMakeChange(coinValueList,change,minCoins):
   for cents in range(change+1):
      coinCount = cents
      for c in coinValueList:
           if(cents >= c):
               if minCoins[cents-c] + 1 < coinCount:
                   coinCount = minCoins[cents-c]+1
      minCoins[cents] = coinCount
   return minCoins[change]


start_time = time.clock()
dpMakeChange([1,5,10,25], 63, [0]*64)
print (time.clock() - start_time, "seconds")


for c in range(3):
    print (c)


def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)
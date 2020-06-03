# bounce.py
#
# Exercise 1.5
startHeight = 60.0
bounceCount = 1
print (startHeight)

while bounceCount<10:
    startHeight=startHeight*.6
    print(round(startHeight))
    bounceCount=bounceCount+1

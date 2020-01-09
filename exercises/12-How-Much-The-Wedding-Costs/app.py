x = int(input('How many people are coming to your wedding?\n'))

if x <= 50:
    price= 4000
if x > 50 and x <= 100:
    price= 10000
if x > 100 and x <= 200:
    price= 15000
if x > 200:
    price= 20000



# Your code above here
print('Your wedding will cost '+str(price)+' dollars')
shopper1Basket = []
shopper2Trolley = []
shelf1 = ["apple", "orange", "banana", "apricot", "mango"]
shelf2 = ["flour", "salt", "sugar", "pepper", "cake mix", "bread"]
conveyor = []
register = {"apple": 1, "orange": 2, "banana": 1, "apricot": 3, "mango":4, "flour":5, "salt":3, "sugar":4, "pepper":3, "cake mix":6, "bread":5}

shopper1TotalCost = 0
shopper2TotalCost = 0

for n in range(len(shelf1)):
    shopper1Basket.append(shelf1.pop())
for n in range(len(shelf2)):
    shopper2Trolley.append(shelf2.pop())
for n in range(len(shopper1Basket)):
    conveyor.append(shopper1Basket.pop())
for n in range(len(conveyor)):
    shopper1TotalCost = shopper1TotalCost + register[conveyor[0]]
    del conveyor[0]
for n in range(len(shopper2Trolley)):
    conveyor.append(shopper2Trolley.pop())
for n in range(len(conveyor)):
    shopper2TotalCost = shopper2TotalCost + register[conveyor[0]]
    del conveyor[0]

print(shopper1TotalCost, shopper2TotalCost)

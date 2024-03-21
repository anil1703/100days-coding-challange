T = int(input())

for i in range(T):
    N = int(input())
    prices = input().split()
    price_count = {}
    
  
    for price in prices:
        if price in price_count:
            price_count[price] += 1
        else:
            price_count[price] = 1
    
    valid = True
    for count in price_count.values():
        if count > 2:
            valid = False
            break
    
    if valid:
        print("Yes")
    else:
        print("No")

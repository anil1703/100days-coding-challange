def check(A,b):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if A <= 3:
        return "YES"
    count = 0
    for char in b:
        if char not in vowels:
            count += 1
        else:
            count = 0
        if count >= 4:
            return "NO"
    return "YES"
    
        
N  = int(input())
for i in range(N):
    A = int(input())
    b = input()
    c = check(A,b)
    print(c)
    

    
t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))  # Problems solved by Om
    b = list(map(int, input().split()))  # Problems solved by Addy
    max_streak_om = 0
    current_streak_om = 0
    max_streak_addy = 0
    current_streak_addy = 0

    for i in range(n):
        if a[i] > 0:
            current_streak_om += 1
        else:
            current_streak_om = 0
        max_streak_om = max(max_streak_om, current_streak_om)
        if b[i] > 0:
            current_streak_addy += 1
        else:
            current_streak_addy = 0
        max_streak_addy = max(max_streak_addy, current_streak_addy)
    if max_streak_om > max_streak_addy:
        print("OM")
    elif max_streak_om < max_streak_addy:
        print("ADDY")
    else:
        print("DRAW")

    t -= 1


def is_vowel(char):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return char in vowels


def can_reach_codetown(s):
    if len(s) != 8:
        return "NO"


    if s[4:] == "TOWN":
        return "YES"


    for i in range(4):
        if (is_vowel(s[i]) and not is_vowel("TOWN"[i])) or (not is_vowel(s[i]) and is_vowel("TOWN"[i])):
            return "NO"
    return "YES"


N = int(input())
for _ in range(N):
    s = input().strip().upper()
    print(can_reach_codetown(s))

words = ["racecar", "rotor", "tomato", "별똥별", "코끼리"]

# 슬라이싱
# if word == word[::-1]:
#     print(True)
# else:
#     print(False)
    
# 투포인터
def palindromes(word: str) -> bool:
    
    s,e = 0, len(word)-1

    while s < e:
        if word[s] != word[e]:
            return False
        else:
            s += 1
            e -= 1
    return True

for word in words:
    print(palindromes(word))
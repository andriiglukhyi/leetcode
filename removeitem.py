s = "abpcplea"
d = ["ale","apple","monkey","plea"]


def dif(s, d):
    match = ''
    counter = 0
    for word in d:
        curent_match = True
        curent = 0
        for item in range(len(word)):
            while curent< len(s) and word[item] != s[curent]:
                curent += 1
            curent += 1
            if curent >= len(s):
                curent_match = False
                break
        if curent_match:
            if len(word) > len(match):
                match = word
            elif len(word) == len(match) and word < match:
                match = word
            
    print(match) 
             

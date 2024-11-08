#Brut Froce Algorithm

def solve(s):
    map = {
        'I' : 1, 'V':5, 'X':10, 'L':50 , 'C' : 100, 'D':500, 'M': 1000,
        'IV': 4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900
    }
    value = 0

    if s in map:
        return map[s]
    else:
        charStr = [s[max(0, len(s) - i - 2):len(s) - i] for i in range(0, len(s), 2)]
        for i in charStr:
            if i in map:
                value += map[i]
            else:
                singleChars = list(i)
                for i in singleChars:
                    if i in map:
                        value += map[i]
        return value
        
  
s = "MCDLXXVI"
print(solve(s))
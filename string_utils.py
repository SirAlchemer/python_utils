
def middle_lexicographical_permutation(string):
    string = sorted(string)
    n = len(string)
    result = []
    
    k = (factorial(n) // 2) - 1
    
    while n > 0:
        n -= 1
        index, k = divmod(k, factorial(n))
        result.append(string.pop(index))
        
    return ''.join(result)

def next_lexicographical_permutation(s: str) -> str:
    s = list(s)
    for i in range(len(s) - 2, -1, -1):
        if ord(s[i]) < ord(s[i + 1]):
            t = s[i:]
            m = min(filter(lambda x:  ord(x) >  ord(t[0]), t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return "".join(s)
    return ""

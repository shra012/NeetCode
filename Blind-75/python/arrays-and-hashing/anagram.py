def isAnagram(s: str, t: str) -> bool:
    fir = {}
    sec = {}
    for c in s:
        if c in fir:
            fir[c] = fir[c] + 1
        else:
            fir[c] = 1
    for c in t:
        if c in sec:
            sec[c] = sec[c] + 1
        else:
            sec[c] = 1

    return fir == sec

if __name__ == "__main__":
    print(isAnagram("racecar", "carrace"))  # True
    print(isAnagram("jar", "jam"))          # False
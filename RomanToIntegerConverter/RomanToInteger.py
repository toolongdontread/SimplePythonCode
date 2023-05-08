def RomanToInteger(s:str) -> int:
    total = 0
    
    if "CM" in s:
        c=s.count("CM")
        s=s.replace("CM", "")
        total+=900*c
    if "CD" in s:
        c=s.count("CD")
        s=s.replace("CD", "")
        total+=400*c
    if "XC" in s:
        c=s.count("XC")
        s=s.replace("XC", "")
        total+=90*c
    if "XL" in s:
        c=s.count("XL")
        s=s.replace("XL", "")
        total+=40*c
    if "IX" in s:
        c=s.count("IX")
        s=s.replace("IX", "")
        total+=9*c
    if "IV" in s:
        c=s.count("IV")
        s=s.replace("IV", "")
        total+=4*c
    if "M" in s:
        c=s.count("M")
        s=s.replace("M", "")
        total+=1000*c
    if "D" in s:
        c=s.count("D")
        s=s.replace("D", "")
        total+=500*c
    if "C" in s:
        c=s.count("C")
        s=s.replace("C", "")
        total+=100*c
    if "L" in s:
        c=s.count("L")
        s=s.replace("L", "")
        total+=50*c
    if "X" in s:
        c=s.count("X")
        s=s.replace("X", "")
        total+=10*c
    if "V" in s:
        c=s.count("V")
        s=s.replace("V", "")
        total+=5*c
    if "I" in s:
        c=s.count("I")
        s=s.replace("I", "")
        total+=1*c
    
    return total

if __name__ == "__main__":
    a = input("Please enter a Roman: ")
    print(RomanToInteger(a))
def romanToDecimal(roman):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman = roman.upper()
    
    dec = 0 
    i = 0
    while i < len(roman):
        if i+1<len(roman):
            if values[roman[i]]<values[roman[i+1]]:
                dec += values[roman[i+1]] - values[roman[i]]
                i += 2
            else:
                dec += values[roman[i]]
                i += 1
        else:
            dec += values[roman[i]]
            i += 1
    
    return dec

print(romanToDecimal("CMXLIV"))
def RomNumber(__NUM__):
    RomeTranslation = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    RomeTranslation_2 = {90: 'XC', 40: 'XL', 9: 'IX', 4: 'IV'}
    RomeStr = ''
    for i in RomeTranslation:
        RomeStr += RomeTranslation[i] * (__NUM__ // i)
        __NUM__ = __NUM__ % i
        for j in RomeTranslation_2:
            if __NUM__ == j:
                RomeStr += RomeTranslation_2[j]
                __NUM__ -= j
    return RomeStr

print(RomNumber(2222))

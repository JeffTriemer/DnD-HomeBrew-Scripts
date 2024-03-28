def d(number, dice):
    import random as rn
    total = 0
    for i in range(number):
        int(rn.randint(1,dice))
        total += int(rn.randint(1,dice))
    return total

def statRoll():
    global stat
    array = []
    for i in range(4):
        array.append( d(1,6))
    stat = sum(array)-min(array)
    return stat

def rollStats():
    import math
    global Str
    global Dex
    global Con
    global Wis
    global Int
    global Cha
    global StrMod
    global DexMod
    global ConMod
    global WisMod
    global IntMod
    global ChaMod
    Str=statRoll()    
    Dex=statRoll()
    Con=statRoll()
    Wis=statRoll()
    Int=statRoll()
    Cha=statRoll()

    StrMod=(Str - 10)/2
    StrMod= math.floor(StrMod)

    DexMod=(Dex - 10)/2
    DexMod=math.floor(DexMod)
    
    ConMod=(Con - 10)/2
    ConMod=math.floor(ConMod)
    
    WisMod=(Wis - 10)/2
    WisMod=math.floor(WisMod)
    
    IntMod=(Int - 10)/2
    IntMod=math.floor(IntMod)
    
    ChaMod=(Cha - 10)/2
    ChaMod=math.floor(ChaMod)
    
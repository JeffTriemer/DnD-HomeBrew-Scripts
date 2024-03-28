exec(open(r"C:\Users\622379\Documents\Python\Homebrew\Script\DiceRoller&RollStats.py").read())


def NPC(number):

    import pandas as pd
    import random as rn
    import datetime as dt

    global s
    global de
    global c
    global w
    global i
    global ch
    global CharacterString
    global AllNPCs
    global Races
    global Pronouns
    global Sexualities
    global Ages
    global Strs
    global Dexes
    global Cons
    global Wises
    global Ints
    global Chas
    global Names
    global AgeDescs
    global Classes
    global Values
    global roles
    global roleDescs
    global PhysicalDescs
    PhysicalDescs= []
    roleDescs=[]
    roles = []
    Values=[]   
    Classes=[]
    AgeDescs =[]
    Names =[]
    Strs = []
    Dexes=[]
    Cons=[]
    Wises=[]
    Ints=[]
    Chas=[]
    Ages= []
    Races = []
    Pronouns = []
    Sexualities = []


    s = 0
    de=0
    c=0
    w=0
    i=0
    ch=0
    
    personalityData = pd.read_excel(r"C:\Users\622379\Documents\Python\Homebrew\DNDRaces.xlsx", sheet_name="12 major personalities")    
    NameData = pd.read_excel(r"C:\Users\622379\Documents\Python\Homebrew\Names.xlsx", sheet_name="Names" )
    LastNameData = pd.read_excel(r"C:\Users\622379\Documents\Python\Homebrew\Names.xlsx", sheet_name="Last Names")
    RoleData = pd.read_csv(r"C:\Users\622379\Documents\Python\Homebrew\TownRoles.csv")
    adjectiveData = pd.read_csv(r"C:\Users\622379\Documents\Python\Homebrew\adjectives.csv")

    

    MasculineNames = NameData[NameData['Gender'] == 'Masculine']
    MasculineNames = MasculineNames['Name'].to_list()
    
    FeminineNames = NameData[NameData['Gender'] == 'Feminine']
    FeminineNames = FeminineNames['Name'].to_list()    
    
    races = 'Dwarf', 'Hill Dwarf', 'Mountain Dwarf', 'Elf', 'High Elf', 'Wood Elf','Drow Elf','Halfling','Lightfoot Halfling', 'Stout Halfling', 'Human', 'Dragonborn', 'Gnome','Forest Gnome','Rock Gnome','Half-Elf','Half-Orc','Tiefling'
    
    ProNouns = 'He/Him', 'She/Her', 'They/Them', 'She/They', 'He/They'
    sexualPreference = 'Masculine', 'Feminine', 'Either'
    classes = 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorceror', 'Warlock', 'Wizard', 'Artificer'
    values = personalityData.Category + ": " +personalityData.Value
    adjectiveData = pd.read_csv(r"C:\Users\622379\Documents\Python\Homebrew\adjectives.csv")

    
    for each in range(number):
        
        eyedesc= adjectiveData['eye descriptors']
        eyedesc = eyedesc.dropna()
        eyedescint = rn.randint(0,len(eyedesc)-1)
        # time.sleep(1)
        eyeDesc = eyedesc[eyedescint]
        # print(eyeDesc)

        eyecolors= adjectiveData['eye colors']
        eyecolors = eyecolors.dropna()
        eyecolorint = rn.randint(0,len(eyecolors)-1)
        # time.sleep(1)
        eyecolor = eyecolors[eyecolorint]
        # print(eyecolor)

        quirks = adjectiveData['quirks']
        quirks = quirks.dropna()
        quirkint = rn.randint(0,len(quirks)-1)
        # time.sleep(1)
        quirk = quirks[quirkint]
        # print(quirk)

        height = adjectiveData['height']
        height = height.dropna()
        heightint = rn.randint(0,len(height)-1)
        # time.sleep(1)
        Height = height[heightint]
        # print(Height)

        haircolors = adjectiveData['haircolors']
        haircolors = haircolors.dropna()
        haircolorint = rn.randint(0,len(haircolors)-1)
        # time.sleep(1)
        haircolor = haircolors[haircolorint]
        # print(haircolor)

        hairlength = adjectiveData['hair length']
        hairlength = hairlength.dropna()
        hairlengthint = rn.randint(0,len(hairlength)-1)
        # time.sleep(1)
        hairlen = hairlength[hairlengthint]
        # print(hairlen)

        flaws = adjectiveData['flaws']
        flaws = flaws.dropna()
        flawint = rn.randint(0,len(flaws)-1)
        # time.sleep(1)
        flaw = flaws[flawint]
        # print(flaw)
        
        PersonalValue = values[rn.randint(0,11)]
        Values.append(PersonalValue)

        raceint = rn.randint(0,17)
        Race = races[raceint]
        Races.append(Race)

        classInt = rn.randint(0,12)
        clas = classes[classInt]
        Classes.append(clas)

        proNounInt = rn.randint(0,4)
        ProNoun = ProNouns[proNounInt]
        Pronouns.append(ProNoun)

        sexualityInt = rn.randint(0,2)
        Sexuality = sexualPreference[sexualityInt]
        Sexualities.append(Sexuality)

        roleInt = rn.randint(0,458)
        role = RoleData.Role[roleInt]
        roles.append(role)
        roleDesc = RoleData.Description[roleInt]
        roleDescs.append(roleDesc)



        rollStats()

        if 'T' in ProNoun:
            nameInt =rn.randint(0,1542)
            Name = NameData.Name[nameInt]    
        elif "He/Him" == ProNoun:
            nameInt =rn.randint(0,940)
            Name = MasculineNames[nameInt]
        elif "She/Her" == ProNoun:
            nameInt =rn.randint(0,600)
            Name = FeminineNames[nameInt]
        else:
            Name = ""
        LastNameInt = rn.randint(0,1139)
        LastName = LastNameData.Last[LastNameInt]
        
        physicalDesc = f'{Name} has {eyeDesc}, {eyecolor} eyes with {hairlen}, {haircolor} hair and is {Height}. {Name} {flaw} and has {quirk}.'
        PhysicalDescs.append(physicalDesc)
        
        Name = Name + " " +LastName

        
        if 'dwarf' in Race.casefold():
            age = rn.randint(0,400)
            Ages.append(age)
            c= 2
            # print(age)
            if age < 51:
                ageDesc = "Child"
            elif age < 150:
                ageDesc = "Young Adult"
            elif age < 250:
                ageDesc = "Middle Aged"
            elif age < 350:
                ageDesc = "Old"
            else:
                ageDesc = "Extremely Old"
        elif 'half-orc' in Race.casefold():
            age = rn.randint(0,80)
            Ages.append(age)
            s=2
            c=1
            # print(age)
            if age < 14:
                ageDesc = "Child"
            elif age < 25:
                ageDesc = "Young Adult"
            elif age < 55:
                ageDesc = "Middle Aged"
            elif age < 75:
                ageDesc = "Old"
            else:
                ageDesc = "Extremely Old"
        elif 'half-elf' in Race.casefold():
            age = rn.randint(0,200)
            Ages.append(age)
            ch= 2
            # +1 to two random abilities?
            
            # print(age)
            if age < 20:
                ageDesc = "Child"
            elif age < 75:
                ageDesc = "Young Adult"
            elif age < 120:
                ageDesc = "Middle Aged"
            elif age < 180:
                ageDesc = "Old"
            else:
                ageDesc = "Extremely Old"
        elif "elf" in Race.casefold():
            age = rn.randint(0,800)
            Ages.append(age)
            de=2
            # print(age)
            if age < 101:
                ageDesc = "Child"
            elif age < 300:
                ageDesc = "Young Adult"
            elif age < 500:
                ageDesc = "Middle Aged"
            elif age < 700:
                ageDesc = "Old"
            else:
                ageDesc = "Extremely Old"
        elif "tiefling" in Race.casefold():
            age = rn.randint(0,125)
            Ages.append(age)
            ch=2
            i=1
            # print(age)
            if age < 18:
                ageDesc = "Child"
            elif age < 35:
                ageDesc = "Young Adult"
            elif age < 65:
                ageDesc = "Middle Aged"
            elif age < 100:
                ageDesc = "Old"
            else:
                ageDesc = "Extremely Old"
        elif "gnome" in Race.casefold():
            age = rn.randint(0,500)
            Ages.append(age)
            i=2
            # print(age)
            if age < 40:
                ageDesc = "Child"
            elif age < 200:
                ageDesc = "Young Adult"
            elif age < 350:
                ageDesc = "Middle Aged"
            elif age < 450:
                ageDesc = "Old"
            else:
                ageDesc = "Extremely Old"
        elif "dragonborn" in Race.casefold():
            age = rn.randint(0,90)
            Ages.append(age)
            s=2
            ch=1
            # print(age)
            if age < 15:
                ageDesc = "Child"
            elif age < 30:
                ageDesc = "Young Adult"
            elif age < 60:
                ageDesc = "Middle Aged"
            elif age < 80:
                ageDesc = "Old"
            else:
                ageDesc = "Extremely Old"
        elif 'halfling' in Race.casefold():
            age = rn.randint(0,160)
            Ages.append(age)
            de=2
            # print(age)
            if age < 20:
                ageDesc = "Child"
            elif age < 60:
                ageDesc = "Young Adult"
            elif age < 100:
                ageDesc = "Middle Aged"
            elif age < 145:
                ageDesc = "Old"
            else:
                ageDesc = "Extremely Old"
        elif 'human' in Race.casefold():
            age = rn.randint(0,105)
            Ages.append(age)
            c=1
            s=1
            de=1
            ch=1
            i=1
            w=1
            # print(age)
            if age < 18:
                ageDesc = "Child"
            elif age < 30:
                ageDesc = "Young Adult"
            elif age < 60:
                ageDesc = "Middle Aged"
            elif age < 90:
                ageDesc = "Old"
            else:
                ageDesc = "Extremely Old"
                
        Names.append(Name)
        Strs.append(Str)
        Cons.append(Con+c)
        Dexes.append(Dex+de)
        Wises.append(Wis+w)
        Ints.append(Int+i)
        Chas.append(Cha+ch)
        AgeDescs.append(ageDesc)
        
        statTable = pd.DataFrame({'Str' : [Str], 'Dex' : [Dex], 'Con' : [Con], 'Wis':[Wis], 'Int':[Int], 'Cha':[Cha]})
        CharacterString = f'Name: {Name}\nProNouns: {ProNoun}\nRace: {Race}\nClass: {clas}\nSexual Preference: {Sexuality}\nAge: {ageDesc}, {age}\n{statTable}\n_________________________________'
    import pandas as pd
    AllNPCs = pd.DataFrame({'Name':Names,'Race': Races,'Age': Ages, 'AgeDesc': AgeDescs, 'Role': roles,'RoleDesc':roleDescs,'Values':Values,'Preferred Class': Classes, 'Pronouns': Pronouns,'Sexual Preference':Sexualities, 'Str': Strs,'Dex':Dexes,'Con':Cons, 'Wis': Wises, 'Int': Ints,'Cha':Chas, 'PhysicalDescs':PhysicalDescs})
    AllNPCs['Session Notes'] = ""

    Today = str(dt.date.today())
    print(Today)
    filepath = f'C://Users//622379//Documents//Python//Homebrew//NPCs Generated//{Today} Session.csv'
    print(filepath)
    AllNPCs.to_csv(filepath, index=False)
    AllNPCs.head()

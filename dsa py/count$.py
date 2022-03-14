string=input()
repeating_string=string[0:2]
newstring=string.replace(repeating_string,'$')
apcount=newstring.count('$')
for i in range(len(newstring)):
    dollarcount=[]
    # while (newstring[i]=='$' and newstring[i+1]=='$'):
    #     pass
    pass

print(newstring,apcount)
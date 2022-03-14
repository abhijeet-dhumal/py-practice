string=input()
reversedString=list(string[ : :-1])
st=''
sign=['#','@']
for i in range(len(string)):
    if string[i]=='#' or string[i]=='@' : 
        for j in sign:
            if string[i]==j:
                reversedString.remove(string[i])
        reversedString.insert(i,string[i])
        
print(''.join(reversedString))
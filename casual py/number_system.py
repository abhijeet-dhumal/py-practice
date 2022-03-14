
sr="227b Baker St,London NW3 6XE7"
sym=['_','#','@','%']
out=[i for i in sr]
m=0
ct=0
for ch in range(len(sr)):
    if sr[ch].isalpha() and sr[ch].islower():
        ct+=1
        if ct%5!=0:
            out[ch]=chr(97+(122-ord(sr[ch]))).lower()
        else:
            out[ch]=chr(97+(122-ord(sr[ch]))).upper()
    if sr[ch].isalpha() and sr[ch].isupper():
        ct+=1
        if ct%5!=0:
            out[ch]=chr(65+(90-ord(sr[ch]))).lower()
        else:
            out[ch]=chr(65+(90-ord(sr[ch]))).upper()

    if sr[ch].isnumeric() and m<len(sym):
        out[ch]=sym[m]
        m+=1
        if m>=4:
            m=0
       
print("".join(out))
   

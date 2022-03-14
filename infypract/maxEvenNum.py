from itertools import permutations
stri=input()
intList= list(set([i for i in stri if i.isnumeric()]))
# ints=''.join(intList)
# nonrepeated=[]
# for i in ints:
#     if i not in nonrepeated:
#         nonrepeated.append(i)
# # nonrepeated.sort(reverse=True)
# max=1
# listPermute=["".join(x) for x in permutations(intList)]
# for i in listPermute:
#     if int(i)>max and int(i)%2==0:
#         max=int(i)
# print(max)
intList.sort(reverse=True)
digits=''.join(intList)
if int(digits) %2==0:
    print(digits)
else:
    for i in range(len(intList)-1,0,-1):
        if int(intList[i])%2==0:
            d=intList[i]
            print(d)
            intList.remove(d)
            print(intList)
            intList.insert(len(intList),d)
            print(intList)
            even=int(''.join(intList))
            print(even)
            break
    else:
        print(-1)




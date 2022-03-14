# Tomya is a girl. She loves Chef Ciel very much.

# Tomya like a positive integer p, and now she wants to get a receipt of Ciel's restaurant whose total price is exactly p. The current menus of Ciel's restaurant are shown the following table.

# Name of Menu	price
# eel flavored water	1
# deep-fried eel bones	2
# clear soup made with eel livers	4
# grilled eel livers served with grated radish	8
# savory egg custard with eel	16
# eel fried rice (S)	32
# eel fried rice (L)	64
# grilled eel wrapped in cooked egg	128
# eel curry rice	256
# grilled eel over rice	512
# deluxe grilled eel over rice	1024
# eel full-course	2048
# Note that the i-th menu has the price 2i-1 (1 ≤ i ≤ 12).

# Since Tomya is a pretty girl, she cannot eat a lot. So please find the minimum number of menus whose total price is exactly p. Note that if she orders the same menu twice, then it is considered as two menus are ordered. (See Explanations for details)

# Input
# The first line contains an integer T, the number of test cases. Then T test cases follow. Each test case contains an integer p.

# Output
# For each test case, print the minimum number of menus whose total price is exactly p.

# Constraints
# 1 ≤ T ≤ 5
# 1 ≤ p ≤ 100000 (105)
# There exists combinations of menus whose total price is exactly p.
# Sample Input
# 4
# 10
# 256
# 255
# 4096
# Sample Output
# 2
# 1
# 8
# 2
# Explanations
# In the first sample, examples of the menus whose total price is 10 are the following:
# 1+1+1+1+1+1+1+1+1+1 = 10 (10 menus)
# 1+1+1+1+1+1+1+1+2 = 10 (9 menus)
# 2+2+2+2+2 = 10 (5 menus)
# 2+4+4 = 10 (3 menus)
# 2+8 = 10 (2 menus)
# Here the minimum number of menus is 2.

# In the last sample, the optimal way is 2048+2048=4096 (2 menus). Note that there is no menu whose price is 4096.
from itertools import combinations
cases=int(input())
menu_prices=[1,2,4,8,16,32,64,128,256,512,1024,2048]
mod_list=[]
while cases>0:
    positive_price=int(input())
    
    # method1 :
    # last_index=menu_prices.index(positive_price)
    lst_elements_till_lastindex=[x for x in menu_prices if x<=positive_price]
    # last_index=8 if positive_price==256
    # [1, 2, 4, 8, 16, 32, 64, 128, 256] till positive_price
    i=len(lst_elements_till_lastindex)-1
    while i>=0:
        if positive_price not in menu_prices or menu_prices[i]<=positive_price:
            if (positive_price % menu_prices[len(lst_elements_till_lastindex)-1]==0) and positive_price not in lst_elements_till_lastindex:
                mod_list.append(lst_elements_till_lastindex[i])
                print(positive_price//max(mod_list))
                break
            else:
                combs=combinations(lst_elements_till_lastindex,i+1)
                for j in combs:
                    if sum(j)==positive_price:
                        print(len(j))
        i-=1
    
    # # method2:
    # if positive_price>2**11:
    #     for i in menu_prices:
    #         if positive_price%i==0:
    #             mod_list.append(i)
    #     print(positive_price//max(mod_list))
    # else:    
    #     ans=str(bin(positive_price).replace("0b",""))
    #     print(ans.count("1")) 
    cases-=1
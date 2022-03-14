# data=[]
# from . import data
# with open(f"{data}.csv","r") as f :
#     for line in f :
#         print(line)
#     pass
rows,cols=map(int,input().split())
for i in range(rows,0,-1):
    for j in range(cols,0,-1):
        print(((j-(i//j))//2)*"-")
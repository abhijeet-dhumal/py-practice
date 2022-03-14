testcase1={
    'input':{
        'descendingList':[13,10,12,6,2,1],
        'query':12
    },
    'output':2
}
testcase2={
    'input':{
        'descendingList':[],
        'query':7
    },
    'output':-1
}
testcase3={
    'input':{
        'descendingList':[9,8,7,6,5,4],
        'query':3
    },
    'output':-1
}
testcase4={
    'input':{
        'descendingList':[9,8,7,6,5,4,1,0,-12,-127],
        'query':-127
    },
    'output':9
}

def locate_number(lis,query):
    position=0
    if len(lis) ==0:
        return -1
    while(position<len(lis)):
        if query not in lis:
            return -1
        if(lis[position]==testcase2['input']['query']):
            return position
        else:
            position+=1

inputlist=testcase1['input']['descendingList']
queryg=testcase1['input']['query']
ans=locate_number(inputlist,queryg)
if ans==testcase1['output']:
    print("Passed")
else:
    print("Failed")
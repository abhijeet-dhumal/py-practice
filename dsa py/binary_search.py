testcase1={
    'input':{
        'descendingList':[13,12,11,8,8,6,6,6,6,3,-127],
        'query': 6
    },
    'output':5
}
def test_location(input_list,ans,input_query):
    previous=ans-1
    while (previous>=0) and (input_list[previous]==input_query):
        ans-=1

    return ans

def binary_search(input_list,input_query):
    
    start=0
    length=len(input_list)
    end=length-1
    if length==0:
        return -1
    while(start<=end):
        mid=int(start+(end-start)/2)
        if input_list[mid]==input_query:
            return mid
        elif input_list[mid]<input_query:
            end=mid-1
        elif input_list[mid]>input_query:
            start=mid+1           
    # return -1

# take all inputs for testcase 
input_list=testcase1['input']['descendingList']
input_query=testcase1['input']['query']
expected_output=testcase1['output']

# take value of location index 
ans=int(binary_search(input_list,input_query))

# check if location is of first occurrence 
print(test_location(input_list,ans,input_query))

# check if ans taken is equal to expected output 
if ans==expected_output:
    print("Passed")
else:
    print("Failed")
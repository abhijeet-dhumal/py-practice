# casual testcases 
testcase1={
    'input':[19,25,19,3,5,6,7,9,11,14],
    'output':3
}
testcase2={
    'input':[5,6,7,8,9,1,2,3,4],
    'output':5
}
# A list that was rotated n times where n is the size of the list 
testcase3={
    'input':[9,8,7,6,5,4,3,2,1],
    'output':0
}
# a list with one element 
testcase4={
    'input':[1],
    'output':0
}
#  for empty list 
testcase5={
    'input':[],
    'output':0
}

#  function to return count of rotations to be performed 
def count_rotations(inputList):
    min=0
    for i in range(len(inputList)):
        if inputList[i]<inputList[min]:
            min=i
    if min==(len(inputList)-1):
        return 0
    if (len(inputList)==1):
        return 0
    return min

# passing input to the function count_rotations 
tests=[testcase1,testcase2,testcase3,testcase4,testcase5]
# check for all test cases 
cases_num=[x for x in range(len(tests))]
for test in tests:
    print(f"testcase {tests.index(test)+1}:",end=" ")
    input_list=test['input']
    expected_output=test['output']

    ans=count_rotations(input_list)
    # check if ans is equal to expected output 
    if expected_output==ans:
        print(f"Returned ans :{ans} , expected ans: {expected_output}",", Passed")
    else:
        print(f"Returned ans :{ans} , expected ans: {expected_output}",", Failed")
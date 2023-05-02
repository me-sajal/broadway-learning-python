#slicing examples
alist = [1,2,3,4,5,6,7,8]
print("the list items are:",alist)
print(alist[2:7]) #this gives [3,4,5,6,7]
print(alist[:7]) #this gives value form 0 to 6th index 
print(alist[0:7]) #this also gives value  from 0 to 6th index  and same as line 4
print(alist[2:]) #this gives value form 2nd index onward
#negative indexing
print(alist[-5:-2]) #this gives elements from -5 index to -3 index
print(alist[2:-3]) # this gives elements from 2 index to -2 index

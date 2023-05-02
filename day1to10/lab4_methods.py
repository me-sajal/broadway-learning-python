#append in list
#list.append()
l1 = ["a", "e", "i", "o"]
l1.append("U")
print(l1)

#extend
#list.extend()
l3 = ['Python ', 'is ']
l4 = ['an ', 'awesome']
l3.extend(l4)
print(l3)

#insert
#list.insert(i,x)
l5 = [1, 2, 3, 4]
print("values of l5 before insert of 9")
l5.insert(2,9)
print("values of l5 after insert of 9")
print(l5)
#remove 
#list.remove()
l5.remove(4)
print("values of l5 after removing 4", l5)
#list.pop() yesh ley values assign garxa
l5.pop(0)
print("values after poping index 0 ", l5) 
#list.clear()
l1.clear()
print("the values of l1 after clearing", l1)
#value asign ways after assign 
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
value = l2.pop(3)
print("the poped item\'s value is :", value)

#list.index(value, start, end)
c = l2.index(3)
print("The value at index 3 is :", c)

vowels = ['a', 'e', 'i', 'o', 'u', 'e']
print("the datas at vowels are:", vowels)
d = vowels.index('e')
print("The value at index e is :", d)
d = vowels.index('e',3)
print("The value at index e after range  or index 3 is :", d)

#list.count(x)
c = vowels.count('e')
print("the count of e at :", vowels, 'is', c)

#list.sort(key=fun, reverse= true )

l=[3,4,5,6,7,2,1,3,5,6,7,8,9,0]
print("values of l before sort:", l)
l.sort()
print("values of l after sort:", l)
l.sort(reverse=True)
print("values of l after reverse sort:", l)

#sort of data list where the tuples of the data are available
t = [(1,3),(7,2),(3,4),(1,1),(7,0)]
print('values before sorting', t)
def get_second_num(data):
    return data[1]

t.sort(key=get_second_num)
print('values after sorting', t)

#reversing list

a = [1,2,3,4,5,3,1]
print(a)
a.reverse()
print('reveresed a is:',a)


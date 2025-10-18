s={1,2,3,4,4,5,5,6,7,8,7,10}
print(s)
s.add(11)
s.add(20)
s.add(30)
s.add(40)
print(s)
print(len(s)) #return length of set 

s.remove(8) #remove an element  in set 
print(s)

s.pop() #delete  element in set 
print(s)

s.clear() #remove all set elements
print(s)


s1={1,2,3,4}
s2={5,6,4}

# # union method:
print(s1.union(s2))

#intersection method:

s1.intersection_update(s2)
print(s1)


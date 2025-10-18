#tuple is a immutable in python

#empty tuple
tup=()
print(tup)
print(type(tup))

#single element in tuple seprated by , otherwise it treat as variable

tup=(1) #treat as a integer

tup=(1,) #treat as a tuple
print(tup)
print(type(tup))

#multiple value in tuple seprated by ,

tup=(1,2,33,25,31)
print(tup)

#you can not change tuple value

tup[2]=10 # not allowed 

#tuple slicing is same a string and list slicing
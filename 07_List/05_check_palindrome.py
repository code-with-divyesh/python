list1=[1,2,3,2,1]
print(list1)

list2=list1.copy()
list1.reverse()

if list1==list2:
  print("list is palindrome")
else:
  print("List is not palindrome")
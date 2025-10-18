# f=open("abc.txt","r")
# data=f.read() #read entire file
# print(data)
# f.close()

#  for read line
# f=open("abc.txt","r")
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# f.close()


#write file

# f=open("abc.txt","w")
# f.write("hello world")

# f.close()

#write file
# f=open("abc.txt","a")
# f.write(" i am divyesh")

# f.close()

# if file not exist then python automatically create a file

# f=open("sample.txt","a")
# f.write("This is sample file")

# f.close()

# f=open("sample.txt","r+")
# f.write("abc")
# print(f.read())
# f.close()

# f=open("sample.txt","w+")
# print(f.read())
# f.write("abc")
# f.close()


# f=open("sample.txt","a+")
# print(f.read())
# f.write("abc")
# f.close()

# with open("sample.txt","r") as f:
#   data=f.read()
#   print(data)

# with open("sample.txt","w") as f:
#   f.write(" hello")

import os
os.remove("xyz.txt")




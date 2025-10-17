no1=int(input("Enter No1:"))
no2=int(input("Enter No2:"))

print(f"Before swapping no1={no1} and no2={no2}")
no1=no1+no2
no2=no1-no2
no1=no1-no2

print(f"after swapping no1={no1} and no2={no2}")
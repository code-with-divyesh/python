dict={"name":"divyesh","code":"209","marks":[50,60,70]}
print(dict["name"])

print(dict.items()) #return all the items of dict
print(dict.keys())# rerurn all the keys of dict
print(dict.values()) # return all the values of dict
print(dict.get("marks")) #return a value and used for errors
new_dict={"age":22}
dict.update(new_dict)
print(dict)
#creat lists, set, tuple and dictionary and alter them
# set_name={1,2.36,"h","Ali"}
# set_name2={1,3,4,5,6}
# set_name.add(528)
# set_name.remove("h")
# print(set_name & set_name2)

dictionary_name={"name":"ali","age":25,3:True}
dictionary_name["item_key"]="item_value"
dictionary_name[1]=8
dictionary_name["age"]=42

if 1 in dictionary_name:
    del dictionary_name[1]
print(dictionary_name)

# for key,value in dictionary_name.items():
#     print(key,value)
    
    
# del dictionary_name["item_key"]
# print(dictionary_name)

# tuple_name=("red", 1, False)
# singleitem_tuple=("glass",)

# print(tuple_name)
# numbers= [4,5,6,7,8]
# fruits= ["apple","banana","cherry"]
# mixed=[2,"cabbage",True]

# sliced_list=numbers[1:3]
# print(sliced_list)

# print(numbers[-3])

# fruits.remove("apple")
# print(fruits)

# del numbers[-4]
# print(numbers) 

# mixed.pop()
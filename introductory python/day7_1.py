from functools import reduce

#using reduce function and lambda together
num=[x for x in range(1,10)]
product=reduce(lambda x,y : x*y , num)
print(product)

#using filter function and lambda together
num=[x for x in range(100)]
even_numbers=filter(lambda x : x%2!=0 , num)
# print(list(even_numbers))

#using the map and lambda function
num=[1,2,3,4]
square=map(lambda x:x**2,num)
# print(list(square))

# [expression for item in iretable if condition]

#create a list of squars
list_of_squares=[x**2 for x in range(11)]
# print(list_of_squares)

# filter even numbers
list_of_evennumbers=[x for x in range(100) if x%2==0]
# print(list_of_evennumbers)

# filter odd numbers
list_of_evennumbers=[x for x in range(100) if x%2!=0]
# print(list_of_evennumbers)

#lambda arguments : expression
add= lambda x,y : x+y
# print(add(3,5))
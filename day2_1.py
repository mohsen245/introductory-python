#example 1 cheching condition
# num=-50
# if(num>0):
#     print("the number is postive")
# elif  (num==0):
#     print ("Zero")
# else:
#     print("negetive number")

#loop through a list
# list_fruits=["apple", "banana", "cherry"]
# for f in list_fruits:
#      print(f)
    
#Loop with range
# for b in range(10):
#     print(b)
    
# Loop by while
# count=5
# a=0
# while count>0:
#     print(count)
#     a+=1
#     if a==10:
#         break
    
# print("finished")


#using Continue in for loop
# for t in range(20):
#     if t%2==1:
#         continue
#     print(t)


# using input and checking prime number
num = int(input("input an integer number"))

if num >1:
    for i in range(2,int(num**0.5)+1):
        print(i)
        if num%i==0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")